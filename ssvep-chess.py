from psychopy import visual, core, event
import math


def create_window():
    return visual.Window([1707, 1067], fullscr=True, units='pix')


def create_boxes(win, rows, cols, box_width, box_height):
    boxes = []
    for row in range(rows):
        for col in range(cols):
            initial_color = 'white' if (row + col) % 2 == 0 else 'black'
            box = visual.Rect(win, width=box_width, height=box_height, fillColor=initial_color, lineColor=initial_color,
                              opacity=1)
            x_pos = (col - cols / 2 + 0.5) * box_width
            y_pos = (row - rows / 2 + 0.5) * box_height
            box.pos = [x_pos, y_pos]
            boxes.append(box)
    return boxes


def update_opacity(boxes, start_time, clock, blink_frequency, duration):
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
    for box in boxes:
        box.draw()
    win.flip()


def main():
    win = create_window()
    boxes = create_boxes(win, 12, 12, 150, 100)
    clock = core.Clock()
    start_time = clock.getTime()
    duration = 60  # 设置变化幅度增大到0.5的持续时间为60秒
    blink_frequency = 10  # 设置闪烁频率为每秒5次

    while True:
        update_opacity(boxes, start_time, clock, blink_frequency, duration)
        draw_boxes(boxes, win)

        if 'escape' in event.getKeys():
            break

    win.close()


if __name__ == '__main__':
    main()
