import sys


def solution(lines):
    op_line = lines[-1]
    num_lines = lines[:-1]
    total = 0
    work = []
    # Convert the test into columns, remember to discard the blank space between columns
    while len(op_line)>0:
        last_op = max( op_line.rfind('*'), op_line.rfind('+') )
        op = op_line[last_op]

        nums = []
        trim_end = last_op-1 if last_op>0 else 0
        for i in range(len(num_lines)):
            nums.append(num_lines[i][last_op:])
            num_lines[i] = num_lines[i][:trim_end]
        op_line = op_line[:trim_end]
        work.append( (op,nums) )

    # Convert the numbers into Cephalopod numbers
    for x in range(len(work)):
        (op,num_str) = work[x]
        nums = []
        for y in range(len(num_str[0])-1,-1,-1):
            n_str = ""
            for ns in num_str:
                if ns[y] != ' ':
                    n_str += ns[y]
            nums.append(int(n_str))
        work[x] = (op,nums)

    # do the math and return the total
    total = 0
    for (op,nums) in work:
        val = nums[0]
        for i in range(1,len(nums)):
            if op == '+':
                val += nums[i]
            elif op == '*':
                val *= nums[i]
        total += val
    
    return total

if __name__ == '__main__':
    print(f"*** Advent of Code 2025, Day 6, Part 2 ***\n")
    fname = sys.argv[1] if len(sys.argv) >=2 else 'sample.txt'
    if(len(sys.argv) >=3 and sys.argv[2] == 'debug'):
        debug = True

    df = open(fname, "r")
    lines = [l for l in df.read().splitlines() if len(l.strip())>0]
    result = solution(lines)
    print(f"Result: {result}")