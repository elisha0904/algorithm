import sys
sys.setrecursionlimit(100000)

# 전위 순회 : V L R
# 후위 순회 : L R V

def solution(nodeinfo):
    nodeinfo = sorted([x, y, i+1] for i, (x, y) in enumerate(nodeinfo))
    answer = [[], []]
    
    def LVR(nodeinfo):
        if nodeinfo:
            root_ = (0, -1, 0)
            for idx, (x, y, n) in enumerate(nodeinfo):
                if y > root_[1]:
                    root_ = (idx, y, n)
            
            answer[0].append(root_[2]) # 전위 선루트
            left, right = nodeinfo[:root_[0]], nodeinfo[root_[0]+1:]
            LVR(left); LVR(right)
            answer[1].append(root_[2])
            
    LVR(nodeinfo)
    
    return answer