# https://programmers.co.kr/learn/courses/30/lessons/60061

def solution(n, build_frame):
    beams = []
    columns = []

    for work in build_frame:
      type = work[2]
      x, y, isBuild = work[0], work[1], work[3]
      if type == 0: # 기둥
        if isBuild == 1:
          if y == 0 or [x,y] in beams or [x-1,y] in beams or [x,y-1] in columns:
            columns.append([x,y])
        else: 
          if [x,y+1] in columns:
            if [x-1,y+1] not in beams and [x,y+1] not in beams:
              continue
          if [x,y+1] in beams:
            if [x+1,y] not in columns:
              if ([x-1,y+1] not in beams or [x+1,y+1] not in beams):
                continue
          if [x-1,y+1] in beams:
            if [x-1,y] not in columns:
              if ([x-2,y+1] not in beams or [x,y+1] not in beams):
                continue
          columns.remove([x,y])
      else:
        if isBuild == 1:
          if [x,y-1] in columns or [x+1,y-1] in columns or ( [x-1,y] in beams and [x+1,y] in beams ):
            beams.append([x,y])
        else:
          if [x,y] in columns and [x-1,y] not in beams and [x,y-1] not in columns:
            continue
          if [x+1,y] in columns and [x+1,y] not in beams and [x+1,y-1] not in columns:
            continue
          if [x+1,y] in beams:
            if [x+1,y-1] not in columns and [x+2,y-1] not in columns:
              continue
          if [x-1,y] in beams:
            if [x-1,y-1] not in columns and [x,y-1] not in columns:
              continue
          beams.remove([x,y])

    answer = []

    for column in columns:
      column.append(0)
      answer.append(column)
    
    for beam in beams:
      beam.append(1)
      answer.append(beam)

    answer.sort(key=lambda x:(x[0],x[1],x[2]))

    return answer


n = 5
# x,y,a,b
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n,build_frame))
