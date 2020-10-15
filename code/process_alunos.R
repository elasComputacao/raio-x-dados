library(magrittr)

.HELP <- "
Rscript process_alunos.R -i <input_path> -e <export_path>
"

# Caminho da pasta com os dados pre-processados
.INPUT_HELP <- "
\t   Ex: \"../inst/extdata/\"
"

# Caminho para salvar os dados de historico 
.EXPORT_HELP <- "
\t   Ex: \"../inst/extdata/\"
"

get_args <- function() {
  args = commandArgs(trailingOnly=TRUE)
  
  option_list = list(
    optparse::make_option(c("-i", "--input_path"),
                          type="character",
                          default="../inst/extdata/",
                          help=.INPUT_HELP,
                          metavar="character"),
    optparse::make_option(c("-e", "--export_path"),
                          type="character",
                          default="../inst/extdata/",
                          help=.EXPORT_HELP,
                          metavar="character")
  );
  
  opt_parser <- optparse::OptionParser(option_list = option_list, usage = .HELP)
  opt <- optparse::parse_args(opt_parser)
  return(opt);
}

args <- get_args()
print(args)

input_path <- args$input_path
export_path <- args$export_path

alunos <- readr::read_csv(paste0(input_path, "/alunos_computacao.csv"))
historico <- readr::read_csv(paste0(input_path, "/historico_computacao.csv"))

join_alunos_historico <- function(alunos_df, historico_df) {
  alunos_df %>%  
    dplyr::left_join(historico_df, by = c("matricula"))
}

generate_ids <- function(x) {
  max.val = x*100
  count <- nchar(as.character(max.val))                       
  size <- paste("%0",count,"d",sep="")
  lets <- toupper(sample(letters,x, replace=T))
  nums <- sprintf(size,sample(1:max.val)[1:x])
  ids <- paste(lets,nums,sep="")
  
  return(ids)
}

historico_alunos <- join_alunos_historico(alunos, historico)

id <- generate_ids(nrow(historico_alunos))
ids <- data.frame(id)

historico_alunos_raiox <- dplyr::bind_cols(ids, historico_alunos) %>% 
  dplyr::select(-cpf,
                -matricula)

readr::write_csv(historico_alunos_raiox, paste0(export_path, "/historico_alunos.csv"))
