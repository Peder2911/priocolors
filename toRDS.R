#!/usr/bin/Rscript
args <- commandArgs(trailingOnly = TRUE)
if(length(args) == 2){
   library(yaml)
   files <- commandArgs(trailingOnly = TRUE)[c(1,2)]
   saveRDS(yaml.load_file(files[1]),files[2])
} else {
   writeLines('Usage: toRDS.R [input.yaml] [output.rds]')
}
