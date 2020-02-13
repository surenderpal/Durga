cart=[10,30,430,550,340,123]
for item in cart:
    if item > 500:
        print("We can't continue with item greater than 500")
        # break
        continue
    print("Processing item",item)
else:
    print("Congratulations you'r shopping is successful!!!!")
