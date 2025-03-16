"""
File:   ssvep_chess.py
Brief:  生成按照固定频率闪烁的棋盘状图案。
Requirements:
        PsychoPy (www.psychopy.org)
Author: 高迎新 材料学院
Created:    2024/05/25
Modified:   2024/05/31

"""
import math
from psychopy import visual, core, event, gui
from psychopy.tools.filetools import fromFile, toFile


def create_window() -> visual.Window:
    """生成4K全屏页面"""
    return visual.Window([1707, 1067], fullscr=True, units='pix', color='black')


def create_boxes(win, rows, cols, box_width, box_height):
    """
    在给定的窗口中创建一个网格布局的方块集合。

    Parameters
    ----------
    win : psychopy.visual.Window
        PsychoPy窗口对象，用于显示所有的方块。
    rows : int
        方块网格的行数。
    cols : int
        方块网格的列数。
    box_width : int
        每个方块的宽度。
    box_height : int
        每个方块的高度。

    Returns
    -------
    list
        包含所有创建的方块对象的列表，每个对象是一个 `visual.Rect` 实例。
    """
    boxes = []
    for row in range(rows):
        for col in range(cols):
            initial_color = 'white' if (row + col) % 2 == 0 else 'black'
            box = visual.Rect(win, width=box_width, height=box_height,
                              fillColor=initial_color, lineColor=initial_color,
                              opacity=1)
            x_pos = (col - cols / 2 + 0.5) * box_width
            y_pos = (row - rows / 2 + 0.5) * box_height
            box.pos = [x_pos, y_pos]
            boxes.append(box)
    return boxes


def update_opacity(boxes, start_time, clock, blink_frequency, duration):
    """
    根据指定的闪烁频率逐渐调整方块的透明度，直到达到指定的持续时间。

    Parameters
    ----------
    boxes : list
        包含PsychoPy visual.Rect对象的列表，每个对象代表一个方块。
    start_time : float
        动画开始的时间，通常是开始运行动画时的时间戳。
    clock : psychopy.clock.Clock
        PsychoPy时钟对象，用于跟踪动画的时间。
    blink_frequency : float
        指定方块闪烁的频率，单位是每秒闪烁次数。
    duration : float
        透明度变化达到最大幅度的总持续时间，单位是秒。

    Returns
    -------
    None
    """
    current_time = clock.getTime()
    elapsed_time = current_time - start_time
    max_alpha_increment = 0.5  # 最大透明度增加量
    alpha_increment = max_alpha_increment * min(elapsed_time / duration, 1)  # 透明度增加量随时间逐渐增大
    blink_period = 1 / blink_frequency  # 计算闪烁周期
    blink_phase = math.floor(current_time / blink_period) % 2  # 计算当前闪烁相位
    alpha_value = 1 - blink_phase * alpha_increment  # 使用当前闪烁相位产生透明度的轻微变化
    for box in boxes:
        box.opacity = alpha_value


def draw_boxes(boxes, win):
    """绘制给定列表中的所有方块到屏幕上，并刷新屏幕。"""
    for box in boxes:
        box.draw()
    win.flip()


def get_experiment_info():
    """
    显示对话框让用户输入实验参数

    Returns
    -------
    dict
        包含用户输入的实验参数
    """
    # 默认值
    exp_info = {
        '闪烁频率 (Hz)': 10,
        '持续时间 (秒)': 60,
        '行数': 12,
        '列数': 12,
    }

    # 尝试从文件加载上次的设置（如果存在）
    try:
        exp_info = fromFile('last_settings.pickle')
    except (IOError, FileNotFoundError, OSError) as e:
        print(f"无法加载上次设置：{e}")

    # 创建对话框
    dlg = gui.DlgFromDict(
        dictionary=exp_info,
        title='闪烁方块实验设置',
        fixed=['固定字段'],
        order=['闪烁频率 (Hz)', '持续时间 (秒)', '行数', '列数', '提示文本字体']
    )

    # 如果用户点击确认，保存设置并返回参数
    if dlg.OK:
        toFile('last_settings.pickle', exp_info)
        return exp_info
    else:
        core.quit()  # 用户取消，退出程序


def show_epilepsy_warning(win):
    """
    在屏幕中心显示光敏性癫痫警告

    Parameters
    ----------
    win : psychopy.visual.Window
        PsychoPy窗口对象

    Returns
    -------
    None
    """
    window_width, window_height = win.size

    # 创建警告框背景
    warning_box = visual.Rect(
        win,
        width=window_width * 0.8,
        height=window_height * 0.6,
        fillColor='black',
        lineColor='red',
        lineWidth=3
    )

    # 警告标题
    warning_title = visual.TextStim(
        win,
        text="光敏性癫痫警告",
        pos=[0, window_height * 0.2],
        color='red',
        height=36,
        bold=True,
        font='Microsoft YaHei'
    )

    # 警告内容
    warning_text = visual.TextStim(
        win,
        text="注意：本实验包含快速闪烁的视觉元素，\n"
             "可能会引起某些人的光敏性反应或癫痫发作。\n\n"
             "如果您有癫痫病史，或对闪烁敏感，\n"
             "请勿参与本实验或立即停止观看。\n\n"
             "如果您在观看过程中出现头晕、恶心、视觉变化、\n"
             "眼或肌肉抽搐、失去意识等不适症状，\n"
             "请立即停止实验并咨询医疗专业人员。",
        pos=[0, 0],
        color='white',
        height=24,
        bold=True,
        font='Microsoft YaHei',
        wrapWidth=window_width * 0.7,
        alignText='center'
    )

    # 确认提示
    confirm_text = visual.TextStim(
        win,
        text="我已阅读并理解上述警告\n按空格键继续，或按ESC键退出",
        pos=[0, -window_height * 0.25],
        color='yellow',
        height=20,
        bold=True,
        font='Microsoft YaHei'
    )

    # 绘制所有元素
    warning_box.draw()
    warning_title.draw()
    warning_text.draw()
    confirm_text.draw()
    win.flip()

    # 等待用户按键
    keys = event.waitKeys(keyList=['space', 'escape'])

    # 如果用户按ESC，退出程序
    if 'escape' in keys:
        win.close()
        core.quit()

def main():
    """创建窗口和方块，启动一个定时循环，用于更新方块的透明度并绘制它们到屏幕上。"""
    # 设置提示字体为“微软雅黑”
    text_font = 'Microsoft YaHei'

    # 获取用户设置的实验参数
    exp_info = get_experiment_info()

    # 从用户输入中获取参数
    blink_frequency = int(exp_info['闪烁频率 (Hz)'])
    duration = int(exp_info['持续时间 (秒)'])
    rows = int(exp_info['行数'])
    cols = int(exp_info['列数'])

    # 创建窗口
    win = create_window()

    # 显示光敏性癫痫警告
    show_epilepsy_warning(win)

    # 根据窗口大小动态调整网格和方块大小
    window_width, window_height = win.size

    # 确定适当的网格尺寸和方块大小
    box_width = window_width / cols
    box_height = window_height / rows

    boxes = create_boxes(win, rows, cols, box_width, box_height)
    clock = core.Clock()
    start_time = clock.getTime()

    # 在窗口中显示当前设置
    settings_text = f"闪烁频率: {blink_frequency} Hz\n持续时间: {duration} 秒\n网格: {rows}×{cols}"
    instruction = visual.TextStim(
        win,
        text=settings_text,
        pos=[0, window_height / 2 - 60],
        color='white',
        height=24,
        font=text_font,  # 设置的字体
        bold=True
    )
    instruction.draw()

    start_instruction = visual.TextStim(
        win,
        text="按任意键开始实验，按ESC随时退出",
        pos=[0, -window_height / 2 + 30],
        color='white',
        height=24,
        font=text_font,  # 使用用户选择的字体
        bold=True
    )
    start_instruction.draw()
    win.flip()

    # 等待用户按键开始
    event.waitKeys()

    while True:
        update_opacity(boxes, start_time, clock, blink_frequency, duration)
        draw_boxes(boxes, win)

        if 'escape' in event.getKeys():
            print("实验被用户中止。")
            break

    win.close()
    core.quit()


if __name__ == '__main__':
    main()