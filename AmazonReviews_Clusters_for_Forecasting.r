meta_automotive <- read.csv("path/meta_automobile.csv")
automotive = na.omit(meta_automotive)
View(automotive)


cluster5 = automotive[automotive$overall=="5",]
cluster4 = automotive[automotive$overall=="4",]
cluster3 = automotive[automotive$overall=="1" | automotive$overall=="2" |automotive$overall=="3" ,]


f1=function(cluster){

  cluster_time = cluster$reviewTime
time_format = gsub(", ", "-",cluster_time,fixed = TRUE)

year = c()
for (i in 1:length(time_format)) year[i] = substring(time_format[i], first = nchar(time_format[i])-3, last = nchar(time_format[i]))
month_day = c()
for (i in 1:length(time_format)) month_day[i] = substring(time_format[i], first = 1, last = nchar(time_format[i])-5)


date_of_Review = paste( year,month_day)
date_of_Review = as.Date(gsub(" ", "-",date_of_Review,fixed = TRUE))
cluster = cbind(cluster, date_of_Review)
cluster = cluster[,-7]
return(cluster)
}
cluster5=f1(cluster5)
cluster4=f1(cluster4)
cluster3=f1(cluster3)
f2=function(cluster){
  tsrating=as.data.frame(table(format(cluster$date_of_Review,"%b-%Y")))
  return(tsrating)
}

tsrating5=f2(cluster5)
tsrating4=f2(cluster4)
tsrating3=f2(cluster3)

write.csv(tsrating3, file = "path/cluster3_review.csv")
write.csv(tsrating4, file = "path/cluster4_review.csv")
write.csv(tsrating5, file = "path/cluster5_review.csv")

write.csv(cluster3, file = "path/cluster3.csv")
write.csv(cluster4, file = "path/cluster4.csv")
write.csv(cluster5, file = "path/cluster5.csv")


