with open("exercise_list.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# The second section starts at line 316 (index 315) and ends at line 333 (index 332)
# But let's just find the first <!-- Footer Stats / Progress Section --> and the second one.
count = 0
out_lines = []
skip = False
for line in lines:
    if "<!-- Footer Stats / Progress Section -->" in line:
        count += 1
        if count == 2:
            skip = True
    
    if skip:
        if "</section>" in line:
            skip = False
        continue
        
    out_lines.append(line)

with open("exercise_list.html", "w", encoding="utf-8") as f:
    f.writelines(out_lines)
