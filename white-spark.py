from psychopy import visual, event, core

# 创建窗口
win = visual.Window([1707, 1067], fullscr=True)

# 设置刺激
num_boxes = 5
box_size = 10
boxes = []
for i in range(num_boxes):
    box = visual.Rect(win, width=box_size, height=box_size, fillColor='white')
    box.pos = [(i - num_boxes // 2) * box_size * 1.5, 0]  # 水平排列
    boxes.append(box)

# 刺激频率（每秒闪烁次数）
frequency = 10
frame_rate = int(win.getActualFrameRate())  # 获取屏幕的帧率
frames_per_cycle = int(frame_rate / frequency)  # 每个周期的帧数

# 实验主循环
for i in range(60 * frames_per_cycle):  # 最多运行60秒
    for _, box in enumerate(boxes):
        if i % frames_per_cycle < frames_per_cycle / 2:
            box.fillColor = 'black'
        else:
            box.fillColor = 'white'
        box.draw()

    win.flip()

    if 'escape' in event.getKeys():
        print("实验被用户中止。")
        break

win.close()
core.quit()
