"""
这个模块提供了使用A*算法解决8数码问题的工具。

该模块提供了表示8数码状态以及使用A*搜索算法解决它的必要类和函数。主要的类是`AStar`
它代表了A*算法及其寻找解决方案路径的方法。
"""

import heapq
from typing import List, Optional, Tuple


class State(object):
    """
    代表搜索问题的通用状态。

    Attributes:
        children (list): 子状态的列表。
        parent (State): 父状态。
        value (list): 表示状态的值。
        dist (int): 从目标的启发式距离。
        path (list): 从开始状态到此状态的路径。
        start (list): 谜题的起始状态。
        goal (list): 谜题的目标状态。
    """

    def __init__(
            self,
            value: List[List[int]],
            parent: Optional['State'],
            start: List[List[int]] = None,
            goal: List[List[int]] = None
    ):
        """
        初始化状态。

        Args:
            value (list): 表示状态的值。
            parent (State): 父状态。
            start (list): 谜题的起始状态。
            goal (list): 谜题的目标状态。

        Returns:
            None
        """
        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0
        if parent:  # 如果有父状态，则继承父状态的路径
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
        else:  # 如果没有父状态，则创建一个新的路径
            self.path = [value]
            self.start = start
            self.goal = goal

    def GetDist(self):
        """
        获取状态的启发式距离。
        """
        pass

    def CreateChildren(self):
        """
        生成子状态。
        """
        pass


class State_8puzzle(State):
    """
    代表8数码问题中的状态。

    这个类扩展了通用的State类，并为8数码问题实现了启发式距离计算和子状态生成。

    属性从`State`类继承。
    """

    def __init__(
            self,
            value: List[List[int]],
            parent: Optional[State],
            start: List[List[int]] = None,
            goal: List[List[int]] = None
    ):
        """
        初始化状态。

        Args:
            value (list): 表示状态的值。
            parent (State): 父状态。
            start (list): 谜题的起始状态。
            goal (list): 谜题的目标状态。
        """
        super(State_8puzzle, self).__init__(value, parent, start, goal)
        self.dist = self.GetDist()

    def GetDist(self) -> int:
        """
        获取状态的启发式距离。

        Args:
            self (State_8puzzle): 代表状态的对象。

        Returns:
            int: 从目标的启发式距离。
        """
        if self.value == self.goal:
            return 0
        dist = 0
        for i in range(3):
            for j in range(3):
                piece = self.value[i][j]
                dist += abs(i - piece // 3) + abs(j - piece % 3)
        return dist

    def CreateChildren(self) -> None:
        """
        生成子状态。

        Args:
            self (State_8puzzle): 代表状态的对象。
        """
        if not self.children:
            i, j = [(i, j) for i in range(3) for j in range(3) if self.value[i][j] == 0][0]
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dir in dirs:
                ni, nj = i + dir[0], j + dir[1]
                if 0 <= ni < 3 and 0 <= nj < 3:
                    val = [row[:] for row in self.value]
                    val[i][j], val[ni][nj] = val[ni][nj], val[i][j]
                    child = State_8puzzle(val, self)
                    self.children.append(child)

    def __lt__(self, other) -> bool:
        """
        比较两个状态的启发式距离。
        """
        return self.dist < other.dist


class AStar:
    """
    代表8数码问题的A*算法。

    Attributes:
        path (list): 从开始到目标的解决方案路径。
        visitedQueue (list): 已访问的状态。
        priorityQueue (PriorityQueue): 待探索的状态，按启发式排序。
        start (list): 谜题的起始状态。
        goal (list): 谜题的目标状态。
    """

    def __init__(
            self, start: List[List[int]],
            goal: List[List[int]]
    ):
        """
        初始化A*算法。
        Args:
            start (list): 谜题的起始状态。
            goal (list): 谜题的目标状态。
        """
        self.path = []
        self.visitedQueue = []
        self.priorityQueue = PriorityQueue()
        self.start = start
        self.goal = goal

    def Solve(self) -> List[List[List[int]]]:
        """
        使用A*算法解决8数码问题。
        Returns:
            list: 从开始到目标的解决方案路径。
        """
        startState = State_8puzzle(self.start, None, self.start, self.goal)
        count = 0
        self.priorityQueue.push(startState)
        while not self.path and self.priorityQueue:
            closestChild = self.priorityQueue.pop()
            closestChild.CreateChildren()
            self.visitedQueue.append(closestChild.value)
            for child in closestChild.children:
                if child.value not in self.visitedQueue:
                    count += 1
                    if not child.dist:
                        self.path = child.path
                        break
                    self.priorityQueue.push(child)
        if not self.path:
            print("Goal not possible!")
        return self.path


class PriorityQueue:
    """
    支持A*算法的优先队列。

    使用Python的heapq模块按其启发式值维护状态。

    Attributes
        queue (list): 按启发式排序的状态列表。
    """
    queue: List[Tuple[int, State]]

    def __init__(self) -> None:
        self.queue = []

    def __len__(self) -> int:
        return len(self.queue)

    def push(self, state) -> None:
        heapq.heappush(self.queue, (state.dist, state))

    def pop(self) -> Optional[State]:
        if self.queue:
            return heapq.heappop(self.queue)[1]
        else:
            return None


def isSolvable(grid: List[List[int]]) -> bool:
    """
    检查给定的8数码问题是否有解。

    Args:
        grid (list): 表示8数码状态的3x3列表。

    Returns:
        bool: 如果问题有解，则为True，否则为False。
    """
    flat_list = [item for sublist in grid for item in sublist]
    inversions = 0

    for i in range(len(flat_list)):
        for j in range(i + 1, len(flat_list)):
            # Don't count zero as it represents the empty space
            if flat_list[i] != 0 and flat_list[j] != 0 and flat_list[i] > flat_list[j]:
                inversions += 1

    return inversions % 2 == 0


def solve(
        start: List[List[int]],
        goal: List[List[int]]
) -> List[List[List[int]]]:
    """
    使用A*算法解决8数码问题。

    Args:
        start (list): 谜题的起始状态。
        goal (list): 谜题的目标状态。

    Returns:
        list: 从开始到目标的解决方案路径。
    """
    if isSolvable(start):
        print("Solving...")
        a = AStar(start, goal)
        a.Solve()
        for i in a.path:
            print(f"step {str(a.path.index(i))}")
            for row in i:
                print(row)
            print("")
        print(f"Solved in {str(len(a.path))} moves.")
        return a.path
    else:
        print("The provided start state is not solvable.")
        return []


if __name__ == "__main__":
    start = [
        [1, 4, 2],
        [3, 0, 5],
        [6, 7, 8]
    ]

    goal = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    solved = solve(start, goal)
