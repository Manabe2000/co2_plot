#!/bin/sh

echo "Please input  date interval>>"
read INTERVAL
mkdir graph
i=`expr 30 / $INTERVAL`
h=1
while [ "$h" -lt "$i" ]
do
    a=`expr 1 + ${INTERVAL} \* $h - ${INTERVAL}`
    b=`expr 1 + $h \* ${INTERVAL}`
    var1="2022-10-"${a} #change
    var2="2022-10-"${b} #change
    echo "var ${h:-not set} ${h:+set}"
    python3 plot_research_graph.py $var1 $var2
    echo "save file!"
    h=$(expr $h + 1)
done
month=_2022_10_  # change
mv graph graph$month$INTERVAL

