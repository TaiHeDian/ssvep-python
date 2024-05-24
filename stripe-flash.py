from psychopy import visual, core, event

# 设置窗口
win = visual.Window([1707, 1067], fullscr=True)
counter = 0
max_trials = 60     # 最大闪烁次数

# 创建刺激
stim = visual.GratingStim(win, size=3, pos=[0,0], sf=5, mask='circle')

# 刺激频率（每秒闪烁次数）
frequency = 5  
frame_rate = int(win.getActualFrameRate())  # 获取屏幕的帧率
frames_per_cycle = int(frame_rate / frequency)  # 每个周期的帧数

# 实验主循环
while counter < max_trials:  # 最多运行60次
    if counter % frames_per_cycle < frames_per_cycle / 2:
        stim.phase += 0.1  # 刺激移动
    stim.draw()
    win.flip()

    if 'escape' in event.getKeys():
        print("实验被用户中止。")
        break

win.close()
core.quit()
