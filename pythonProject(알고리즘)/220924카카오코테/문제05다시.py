def solution(commands):
    answer = []
    arr = [[None] * 51 for _ in range(51)]
    merge = [[None] * 51 for _ in range(51)]
    # commands 돌면서 명령어 확인 후 arr에 반영하기
    for idx in range(len(commands)):
        cmd, *cmd_val = commands[idx].split()  # cmd_val : list 형태 [r, c, val] / [r, c] / [val1, val2] 등
        # UPDATE : r c val / val1 val2인 경우로 나누어짐
        if cmd == 'UPDATE':
            if len(cmd_val) == 3:
                r, c, val = int(cmd_val[0]), int(cmd_val[1]), cmd_val[2]
                arr[r][c] = val
            else:
                val1, val2 = cmd_val[0].cmd_val[1]
                for i in range(51):
                    for j in range(51):
                        if arr[i][j] == val1:
                            arr[i][j] = val2
        # MERGE : 범위 안에 값이 하나만 존재할 때 / 값이 여러개 존재할 때 / 값이 없을 때
        elif cmd == 'MERGE':
            r1, c1, r2, c2 = int(cmd_val[0]), int(cmd_val[1]), int(cmd_val[2]), int(cmd_val[3])
            merge_lst = []
            # (r1, c1)에 값이 있을 경우 merge_lst에 위치랑 해당 값 저장 해주기
            if arr[r1][c1]:
                merge_lst.append([(r1, c1), arr[r1][c1]])
            # (r1, c1)에 값이 없을 경우
            else:
                for i in range(51):
                    for j in range(51):
                        # (i, j)가 범위 안에 있는지 확인하고, 해당 arr에 값이 존재하는지 확인
                        if (r1 <= i <= r2 or r2 <= i <=r1) and (c1 <= j <= c2 or c2 <= j <=c1):
                            # 값이 존재하면 merge_lst에 (i, j)위치랑 해당 값 저장해주기
                            if arr[i][j]:
                                merge_lst([(i, j), arr[i][j]])
            # 병합
            for i in range(51):
                for j in range(51):
                    # (i, j)가 범위 안에 있을 때만 병합 해주면 됨
                    if (r1 <= i <= r2 or r2 <= i <= r1) and (c1 <= j <= c2 or c2 <= j <= c1):
                        # merge[i][j]에 값이 없는 경우
                        if not merge[i][j]:
                            # merge_lst에 저장된 값이 없는경우에는 (r1, c1)으로 병합만 해주기
                            if not merge_lst:
                                merge[i][j] = (r1, c1)
                            # 값이 하나라도 있을 때는 그 값으로 병합되었다는 것 기록 후 arr에 반영해주기
                            # 값이 하나든 여러개든 제일 앞에 기록 된 것으로 병합됨!
                            else:
                                merge[i][j] = merge_lst[0][0]
                                arr[i][j] = merge_lst[0][1]
                        # merge[i][j]에 저장된 값이 이미 있을 때
                        else:
                            for x in range(51):
                                for y in range(51):
                                    if merge[x][y] == merge[i][j]:
                                        if merge_lst:
                                            merge[x][y] = merge_lst[0][0]
                                            arr[x][y] = merge_lst[0][1]
                                        else:
                                            merge[x][y] = (r1, c1)
        # UNMERGE : 병합 해제, 값을 갖고 있었다면 (r, c)가 해당 값 가지게 됨
        elif cmd == 'UNMERGE':
            r, c = int(cmd_val[0]), int(cmd_val[1])
            unmerge = merge[r][c]
            unmerge_val = arr[r][c]
            # merge 배열 -(i, j)형태로 기록됨- 돌면서 unmerge랑 값이 같으면서,
            # arr의 값도 같은애 찾아 초기값으로 되돌려주기 (r, c)는 제외
            for i in range(51):
                for j in range(51):
                    if merge[i][j] == unmerge and arr[i][j] == unmerge_val and i != r and j != c:
                        merge[i][j] = None
                        arr[i][j] = None
        # PRINT : arr가 비어있으면(None) 'EMPTY' / 값이 있으면 해당 값 answer에 저장
        elif cmd == 'PRINT':
            r, c = int(cmd_val[0]), int(cmd_val[1])
            if arr[r][c]:
                answer.append(arr[r][c])
            else:
                answer.append('EMPTY')
    return answer


result = solution(
    ['UPDATE 1 1 a', 'UPDATE 1 2 b', 'UPDATE 2 1 c', 'UPDATE 2 2 d', 'MERGE 1 1 1 2', 'MERGE 2 2 2 1', 'MERGE 2 1 1 1',
     'PRINT 1 1', 'UNMERGE 2 2', 'PRINT 1 1'])
print(result)