g++ $2 -lm -pthread
if [ -f "./a.out" ]
then
    counter=1
    for file in $1/input*
    do
        ./a.out < $1/input$counter > $1/myoutput$counter
        cp $1/myoutput$counter $1/temp_myoutput
        cp $1/output$counter $1/temp_output

        sed -i -e 's/[\t \n]//g;/^$/d' $1/temp_output
        sed -i -e 's/[\t \n]//g;/^$/d' $1/temp_myoutput
        
        diff -w $1/temp_myoutput $1/temp_output > /dev/null
        error=$?
        
        if [ $error -eq 0 ]
        then
            echo "Testcase# $counter  :AC"
            echo '\n'            
            rm $1/myoutput$counter
        elif [ $error -eq 1 ]
        then
            echo "Testcase# $counter  :WA"
            echo "Expected"
            cat "$1/output$counter"
            echo "Output"
            cat "$1/myoutput$counter"
            echo '\n'
        fi
        counter=$((counter+1))
    done
    rm a.out
    rm $1/temp_myoutput
    rm $1/temp_output
fi
exit