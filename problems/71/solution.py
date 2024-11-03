class Solution:
    def simplifyPath(self, path: str) -> str:
        path_items = path.split("/")
        stack = list()

        for p in path_items:
            if len(p) == 0 or p == ".":
                continue
            elif p == "..":
                if len(stack):
                    stack.pop()
            else:
                stack.append(p)
        
        return "/"+"/".join(stack)
