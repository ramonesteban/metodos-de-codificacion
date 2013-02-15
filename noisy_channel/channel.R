plot_bubbles <- function() {
    postscript("channel_bubbles.eps")
    data <- read.table("channel.dat", sep = " ")
    circles_radius <- sqrt(data$V3/pi)
    symbols(data$V1, data$V2, circles = circles_radius,
            inches = 0.35, fg = "white", bg = "#336699",
            xlab = "Word length", ylab = "Frecuency of zeros",
            main = "Average porcentage of correct transmitions")
    dev.off()
}

plot_byzerofreq <- function(freq) {
    postscript(paste("channel_byzerofreq", freq*10, ".eps", sep = ""))
    data <- read.table("channel.dat", sep = " ")
    data <- subset(data, data$V2 == freq)
    plot(data$V1, data$V3, type = "l")
    dev.off()
}

plot_bubbles()
plot_byzerofreq(0.1)
plot_byzerofreq(0.2)
plot_byzerofreq(0.3)
plot_byzerofreq(0.4)
plot_byzerofreq(0.5)
plot_byzerofreq(0.6)
plot_byzerofreq(0.7)
plot_byzerofreq(0.8)
plot_byzerofreq(0.9)

