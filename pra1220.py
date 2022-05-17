

rawfile = open("Tian_m54139_180927_081410.subreads.am","r")
outfile = open("10813837file.sam","w")

header = ""
zwmfile = ""
for line in rawfile.readlines()[0:5]:
    header = header + line
rawfile.seek(0)
for line in rawfile.readlines()[5:]:
    if "10813837" in line:
        zwmfile = zwmfile + line

outfile.write(header + zwmfile)
rawfile.close()
outfile.close()