frame_num = int(input())
frames = []
recommend_num = int(input())
recommends = list(map(int, input().split()))

for recommend in recommends:
    # 프레임에 있는 경우
    if recommend in (frame[0] for frame in frames):
        for frame in frames:
            if frame[0] == recommend:
                frame[1] += 1
                break
        continue
    
    # 프레임이 덜 차서 추가하는 경우
    if len(frames) < frame_num:
        frames.append([recommend, 1])
        continue

    # 다른 학생의 사진을 내려야 하는 경우
    min_val_of_frame = min(frame[1] for frame in frames)
    for idx, frame in enumerate(frames):
        if frame[1] == min_val_of_frame:
            frames.remove(frame)
            frames.append([recommend, 1])
            break

for frame in sorted(frames):
    print(frame[0], end=' ')
