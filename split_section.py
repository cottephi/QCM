import os
import collections

authors = ["Philippe","Christopher","Antoine"]

subsections = collections.OrderedDict()

for author in authors:
  ifile = open("./"+author+"/main_"+author+".tex")
  lines = ifile.readlines()
  if os.path.isdir("./"+author+"/section"):
    os.system("rm -r ./"+author+"/section")
  os.system("mkdir ./"+author+"/section")
  curr_section = ""
  curr_subsection = ""
  section_changed = False
  subsection_changed = False

  for line in lines:
    line = line.split("\n")[0]
    full_line = line[:]
    if "\\section" in line:
      line = line[:-1].replace("\t","")
      old_line = line
      for ch in old_line:
        if ch == " ":
          line = line[1:]
        else:
          break
      section = line.replace("\\section{","").lower().replace("}","")
      section = section.replace("é","e")
      section = section.replace("è","e")
      section = section.replace("à","a")
      section = section.replace("ç","c")
      section = section.replace(" ","_")
      section = section.replace("$","")
      section = section.replace("(","")
      section = section.replace(")","")
      section = section.replace("î","i")
      section = section.replace("â","a")
      section = section.replace("ê","e")
      section = section.replace("\'","")
      section = section.replace("\\","")
      section = section.replace("/","")
      section = section.replace(":","_")
      section = section.replace(",","_")
      section = section.replace("?","_")
      section = section.replace("~","_")
      section_changed = True
      if not os.path.isdir("./"+author+"/section/"+section):
        os.system("mkdir ./"+author+"/section/" + section)
        if not section in subsections:
          subsections[section] = []
      curr_section = section
      
    elif "\\subsection" in line:
      line = line[:-1].replace("\t","")
      old_line = line
      for ch in old_line:
        if ch == " ":
          line = line[1:]
        else:
          break
      subsection = line.replace("\\subsection{","").lower().replace("}","")
      subsection = subsection.replace("é","e")
      subsection = subsection.replace("è","e")
      subsection = subsection.replace("à","a")
      subsection = subsection.replace("ç","c")
      subsection = subsection.replace(" ","_")
      subsection = subsection.replace("$","")
      subsection = subsection.replace("(","")
      subsection = subsection.replace(")","")
      subsection = subsection.replace("î","i")
      subsection = subsection.replace("â","a")
      subsection = subsection.replace("ê","e")
      subsection = subsection.replace("’","")
      subsection = subsection.replace("\'","")
      subsection = subsection.replace("\\","")
      subsection = subsection.replace("/","")
      subsection = subsection.replace(":","_")
      subsection = subsection.replace(",","_")
      subsection = subsection.replace("?","_")
      subsection = subsection.replace("~","_")
      subsection_changed = True
      if not os.path.isfile("./"+author+"/subsection/" + curr_section + "/" + subsection):
        os.system("touch ./"+author+"/section/" + curr_section + "/" + subsection + ".tex")
        subsections[section].append(subsection)
      curr_subsection = subsection
    
    elif curr_section != "" and curr_subsection != "" and not "end{document}" in full_line:
      if section_changed and not subsection_changed:
        continue
      
      section_changed = False
      subsection_changed = False
      testline = full_line.replace("\t","").replace(" ","")
      if testline != "":
        ofile = open("./"+author+"/section/" + curr_section + "/" + curr_subsection + ".tex","a")
        ofile.write(full_line+"\n")
        ofile.close()
        
everyone = open("./everyone.tex","w")
everyone.write("\\documentclass[11pt]{article}\n \n")
everyone.write("\\input{headers}\n")
everyone.write("\\begin{document}\n")
everyone.write("\\tableofcontents\n")

for section in subsections:
  everyone.write("  \\section{"+section.replace("_"," ")+"}\n")
  for subsection in subsections[section]:
    everyone.write("    \\subsection{"+subsection.replace("_"," ")+"}\n")
    for author in authors:
      if os.path.isdir("./" + author + "/section/" + section):
        if os.path.isfile("./" + author + "/section/" + section + "/" + subsection + ".tex"):
          everyone.write("      \\input{" + author + "/section/" + section + "/" + subsection + "}\n")
          
everyone.write("\\end{document}\n")
everyone.close()
