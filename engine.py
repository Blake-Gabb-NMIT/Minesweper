def renderScreen(screen):
    while True:
        rows = 0 
        for row in screen:
            rows += 1
            render = str(rows)
            for block in row:
                render += block + " "
            print(render)
        bottomrow = 1
        render = " "
        while bottomrow < rows+1:
            render += str(bottomrow) + "  "
            bottomrow += 1
        print(render)

        input("done")