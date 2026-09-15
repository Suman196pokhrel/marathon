class Node:
    def __init__(self, value: int) -> None:
        self.data: int = value
        self.next: Node | None = None

    def __str__(self) -> str:
        data: str = str(self.data)
        pointer: str = "*" if self.next else "None"
        pointer_len: int = 8 if pointer == "*" else 11
        
        top: str = "-" + "-" * len(data) + "-" * pointer_len + "-"
        mid: str = f"|  {data} | {pointer}  |"
        bot: str = "-" + "-" * len(data) + "-" * pointer_len + "-"
        return "\n".join([top, mid, bot])


class SingleLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.n: int = 0

    def __len__(self) -> int:
        return self.n

    def __str__(self) -> str:
        if self.n == 0:
            return ""
        
        top: list[str] = []
        mid: list[str] = []
        bot: list[str] = []
        
        curr: Node | None = self.head
        while curr is not None:
            val: str = str(curr.data)
            ptr: str = "*" if curr.next is not None else "None"
            w1: int = len(val) + 2
            w2: int = len(ptr) + 2
            
            top.append("┌" + "─" * w1 + "┬" + "─" * w2 + "┐")
            mid.append(f"│ {val} │ {ptr} │")
            bot.append("└" + "─" * w1 + "┴" + "─" * w2 + "┘")
            curr = curr.next

        return "\n".join(["  ".join(top), "->".join(mid), "  ".join(bot)])

    def insert_head(self, value: int) -> None:
        new_node: Node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n += 1

    def insert_at_index(self, idx: int, value: int) -> None:
        if not isinstance(idx, int):
            raise TypeError("index must be an integer")
        if idx == 0 or idx >= self.n:
            raise IndexError("Invalid index provided")

        current: Node | None = self.head
        for _ in range(idx - 1):
            if current is not None:
                current = current.next

        if current is not None:
            node: Node = Node(value)
            node.next = current.next
            current.next = node
            self.n += 1
        
    def append(self, value: int) -> None:
        node: Node = Node(value)

        if len(self) == 0:
            self.insert_head(value)
            return

        current: Node | None = self.head
        while current is not None and current.next is not None:
            current = current.next

        if current is not None:
            current.next = node
            self.n += 1

    def clear(self) -> None:
        self.head = None
        self.n = 0

    def delete_head(self) -> Node:
        if self.n == 0 or self.head is None:
            raise IndexError("Deleting from empty list")

        removed: Node = self.head
        self.head = self.head.next
        self.n -= 1
        return removed

    def delete_tail(self) -> Node | None:
        if self.n == 0:
            raise IndexError("Deleting from empty list")

        elif self.n == 1:
            return self.delete_head()

        current: Node | None = self.head
        while current is not None and current.next is not None and current.next.next is not None:
            current = current.next

        if current is not None and current.next is not None:
            removed: Node = current.next
            current.next = None
            self.n -= 1
            return removed
        return None

    def delete_by_value(self, value: int) -> None:
        if self.n == 0 or self.head is None:
            raise IndexError("Deleting in an empty linkedlist")

        # Match at head
        if self.head.data == value:
            removed: Node = self.head
            self.head = self.head.next
            removed.next = None
            self.n -= 1
            return

        # Match after head
        current: Node | None = self.head.next
        prev: Node = self.head
        while current is not None:
            if current.data == value:
                prev.next = current.next
                current.next = None
                self.n -= 1
                return

            prev = current
            current = current.next

    def delete_by_index(self, idx: int) -> Node:
        if self.n == 0 or self.head is None:
            raise IndexError("Indexing on empty linkedlist")

        if idx >= self.n or idx < 0:
            raise IndexError("Index out of range") 

        if idx == 0:
            removed: Node = self.head
            self.head = self.head.next
            self.n -= 1
            return removed

        curr: Node | None = self.head
        for _ in range(idx - 1):
            if curr is not None:
                curr = curr.next

        if curr is not None and curr.next is not None:
            removed = curr.next
            curr.next = curr.next.next
            self.n -= 1
            return removed
        
        raise IndexError("Index out of range")

    def search_by_value(self, value: int) -> int:
        curr: Node | None = self.head
        counter: int = 0
        while curr is not None:
            if curr.data == value:
                return counter
            counter += 1
            curr = curr.next

        raise ValueError(f"{value!r} not in list")

    def __getitem__(self, key: int) -> int:
        if self.n == 0:
            raise IndexError("Indexing on empty list")

        if key < 0 or key >= self.n:
            raise IndexError("Index out of range")

        curr: Node | None = self.head
        for _ in range(key):
            if curr is not None:
                curr = curr.next

        if curr is not None:
            return curr.data
        raise IndexError("Index out of range")

    def detect_cycle(self) -> bool:
        if self.head is None or self.head.next is None :
            return False


        slow: Node | None  = self.head
        fast: Node | None  = self.head


        # Moving both pointer at diff speed
        while fast is not None and fast.next is not None:
            
            slow = slow.next 
            fast = fast.next.next

            if slow is slow:
                return True

        return False




n1 = Node(11)
print(n1)
