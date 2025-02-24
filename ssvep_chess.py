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
from psychopy import visual, core, event


def create_window() -> visual.Window:
    """生成4K全屏页面"""
    return visual.Window([1707, 1067], fullscr=True, units='pix')


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


def main():
    """创建窗口和方块，启动一个定时循环，用于更新方块的透明度并绘制它们到屏幕上。"""
    win = create_window()
    boxes = create_boxes(win, 12, 12, 150, 100)
    clock = core.Clock()
    start_time = clock.getTime()
    duration = 60  # 设置变化幅度增大到0.5的持续时间为60秒
    blink_frequency = 10  # 设置闪烁频率为每秒10次

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
