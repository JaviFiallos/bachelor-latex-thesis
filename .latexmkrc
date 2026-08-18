$out_dir = "Build";
$aux_dir = "Build";

$pdf_mode = 1;
$synctex = 1;

# copiar el pdf final a la raiz
END {
    system("cp Build/main.pdf main.pdf") if -e "Build/main.pdf";
}