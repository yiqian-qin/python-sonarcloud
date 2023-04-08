
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [collections.Counter()]
        i = 0
        n = len(formula)
        while i < n:
            if formula[i] == '(':
                # Add new empty counter when we find opening bracket
                stack.append(collections.Counter())
                i += 1
            elif formula[i] == ')':
                # merge the top two counters into one, when we find closing bracket
                top = stack.pop()
                i += 1
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[i_start:i] or 1)
                for name,cnt in top.items():
                    stack[-1][name] += cnt * count
            else:
                # We have an atom name, so we find the full name
                i_start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                name = formula[i_start:i]
                
                # We find count of the atom, and set the count
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[i_start:i] or 1)
                stack[-1][name] += count
        # Sort the keys and, and join in a certain format, and return as string
        return ''.join(name + (str(stack[-1][name]) if stack[-1][name] > 1 else '')
                       for name in sorted(stack[-1]))
