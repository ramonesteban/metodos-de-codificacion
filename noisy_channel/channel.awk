{
    sum += $1
    counter++
}
END {
    print sum/counter
}
