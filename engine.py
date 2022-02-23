


def renderScreen(screen): #this goes thru the 2d array and prints it out
        rows = 0 
        for row in screen: # this loops thru the rows of the array
            rows += 1
            render = str(rows)

            for block in row: # loops thru the items in the row
                render += block + " " # adds them to a block to render
            
            print(render) # just a print statement to print the line

        bottomrow = 1
        render = " "

        while bottomrow < rows+1:
            render += str(bottomrow) + "  "
            bottomrow += 1

        print(render)
        return