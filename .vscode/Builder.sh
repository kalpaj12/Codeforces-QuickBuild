g++ $2 -lm
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
            cp $1/myoutput$counter $1/temp2_myoutput
            cp $1/output$counter $1/temp2_output
            sed -i -e ':a;$!{N;s/\n/ /;ba;}' $1/temp2_myoutput
            sed -i -e ':a;$!{N;s/\n/ /;ba;}' $1/temp2_output
            diff $1/temp2_myoutput $1/temp2_output > /dev/null
            e2=$?
            if [ $e2 -eq 0 ]
            then
                echo "Testcase #$counter: AC\n"
                rm $1/myoutput$counter
            else
                echo "Testcase #$counter: ==WA=="
                echo "Expected:"
                cat "$1/output$counter"
                
                if [ -z "$(tail -c 1 "$1/output$counter")" ]
                then
                    echo "\n==EOF==\n"
                else
                    echo "\n==EOF==\n"
                fi
                
                echo "Output:"
                cat "$1/myoutput$counter"
                echo "\n==EOF==\n"
            fi
        elif [ $error -eq 1 ]
        then
            echo "Testcase #$counter: ==WA=="
            echo "Expected:"
            cat "$1/output$counter"
            
            if [ -z "$(tail -c 1 "$1/output$counter")" ]
            then
                echo "==EOF==\n"
            else
                echo "\n==EOF==\n"
            fi
            echo "Output:"
            cat "$1/myoutput$counter"
            echo "\n==EOF==\n"
            
        fi
        counter=$((counter+1))
    done
    rm a.out
    rm $1/temp_myoutput
    rm $1/temp_output
    rm $1/temp2_output
    rm $1/temp2_myoutput
fi
exit