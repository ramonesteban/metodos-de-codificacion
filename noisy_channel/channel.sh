limit=512
potency=0
length=1
words=20
repetitions=30
zeros_occur=0.8
ones_occur=0.9

touch channel.dat
rm channel.dat
touch channel.dat

while [[ length -le limit ]]
do
    echo Running with length $length
    for zero_freq in 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9
    do
        echo And frequency of zeros $zero_freq
        touch temp.dat
        rm temp.dat
        touch temp.dat
        iteration=1
        while [[ iteration -le words ]]
        do
            response=`python channel.py $length $repetitions $zero_freq $zeros_occur $ones_occur`
            echo $response >> temp.dat
            iteration=$(($iteration+1))
        done
        response=`awk -f channel.awk -v len=$length -v zero_freq=$zero_freq temp.dat`
        echo $potency $zero_freq $response >> channel.dat
        rm temp.dat
    done
    echo '' >> channel.dat
    length=$(($length*2))
    potency=$(($potency+1))
done
res=`gnuplot channel.plot`
res=`Rscript channel.R`
