class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        # Intuition - As we add them to our stack, keep track of the span per
        # day, reset if the new price/day is larger than the top of the stack, otherwise
        # its span is the +1 the previous

        span = 1

        # Check the price of the top to see if our new price is less than
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop() # Remove from stack
        
        # We add our default 1 if there is no current stack, monotonic decreasing stack.
        self.stack.append((price, span))
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)