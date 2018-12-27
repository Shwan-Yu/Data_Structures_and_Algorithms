class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        # space O(n) n is the length of the snake or food
        from collections import deque
        self.m, self.n = height, width
        start = (0,0)
        self.snake = deque([start])
        self.memo = set([start])
        self.food = deque(food)
        # careful with the pos, not coordinate
        self.pos = {"U":(-1,0), "L": (0,-1), "R":(0,1), "D":(1,0)}

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        # O(1)
        # pop out tail in case head appear immediately at tail's position
        head = self.snake[0]
        next_pos = (head[0]+self.pos[direction][0],head[1]+self.pos[direction][1])
        tail = self.snake.pop()
        self.memo.remove(tail) # no order in set
        # check if valid
        if not(0<=next_pos[0]<self.m and 0<=next_pos[1]<self.n) or next_pos in self.memo:
            return -1
        self.snake.appendleft(next_pos)
        self.memo.add(next_pos)
        # check if have food
        food = tuple(self.food[0]) if self.food else None
        if food and next_pos == food:
            self.food.popleft()
            self.snake.append(tail)
            self.memo.add(tail)
        return len(self.snake) - 1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
