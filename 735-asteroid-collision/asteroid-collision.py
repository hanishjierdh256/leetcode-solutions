class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for asteroid in asteroids:
            asteroidalive = True
            while asteroidalive:
                if stack:
                    if stack[-1] > 0 and asteroid < 0:
                        if asteroid > 0:
                            stack.append(asteroid)
                            asteroidalive = False
                        elif asteroid < 0:
                            if stack[-1] < -asteroid:
                                stack.pop()
                            elif stack[-1] == -asteroid:
                                stack.pop()
                                asteroidalive = False
                            else:
                                asteroidalive = False
                    else:
                        stack.append(asteroid)
                        asteroidalive = False
                else:
                    stack.append(asteroid)
                    asteroidalive = False
        return stack



