from inputs import  input_day2

dimensions = [list(map(int, row.split("x"))) for row in input_day2.strip().split("\n")]

wrapper = 0
ribbon = 0
for box in dimensions:
    wrapper += 2*box[0]*box[1] + 2*box[0]*box[2] + 2*box[1]*box[2] + min(box[0]*box[1],box[0]*box[2],box[1]*box[2])
    ribbon += box[0]*box[1]*box[2]
    box.remove(max(box))
    ribbon += 2*(box[0]+box[1])

print(f"First Solution: {wrapper}")
print(f"Second Solution: {ribbon}")