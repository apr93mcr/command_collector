
import os
from datetime import datetime

os.chdir("C:/Users/Admin/Documents/Alejandro/Programing/Python_folder/commands_collector/")
os.getcwd()

commands = {
    "Linux": [
        {"command": "ls -la", "description": "List files with details"},
        {"command": "grep 'text' file", "description": "Search for text in a file"},
    ],
    "Python": [
        {"command": "print('Hello')", "description": "Print text to console"},
    ],
    "Conda": [
        {"command": "conda env list", "description": "list conda enviroments"},
    ],
    "Git": [
        {"command": "git add file.txt", "description": "Add a file on git"},
    ],
    "R": [
        {"command": "summary(df)", "description": "Get summary statistics of a dataframe"},
    ],
    "Snakemake": [
        {"command": "snakemake --cores 4", "description": "Run workflow using 4 cores"},
    ]
}

#------------------------------------------------------------------------------------------------------------------
#Linux commands
commands["Linux"].append({
    "command": "du -hs folder_path", "description": "Display the total size of a folder"
})

commands["Linux"].append({
    "command": "df -h", "description": "Display the used and available memory space of the server"
})

commands["Linux"].append({
    "command": "df -h --type=ext4 --type=xfs --type=btrfs", "description": "Shows only typical physical disk filesystems"
})

commands["Linux"].append({
    "command": "tmux new-session -s name_session", "description": "create a new tmux session"
})

commands["Linux"].append({
    "command": "tmux attach-session -t name_session", "description": "attach a tmux session"
})

commands["Linux"].append({
    "command": "ps aux | grep server.py", "description": "identify an ongoing job"
})

commands["Linux"].append({
    "command": "screen -d -m -L python server.py", "description": "run a process in the background"
})

commands["Linux"].append({
    "command": "for i in {1..2}; do echo batch$i; samtools merge -f combined_BAMs/R-2013-2166.batch$i.bam *batch$i_*.bam; done", "description": "Concatenate bam files"
})

commands["Linux"].append({
    "command": "awk '{ if ($1 ~ /^#/ || $7 == 'PASS') print $0 }' input.vcf > filtered.vcf", "description": "Filter PASS variants from a vcf file"
})

commands["Linux"].append({
    "command": "infer_experiment.py -r /home/alejandro/hg19/hg19_refseq.bed -i /mnt/storage2/sequencing/WTS/250411_A01183_0662_AH3YTFDMX2/BAMs/E-2018-58210_RNA_85248.bam", "description": "Infer the RNA setting of WTS bam file"
})

commands["Linux"].append({
    "command": "awk 'BEGIN{OFS=\t} {gsub(/^chr/, "", $1); print $1, $2, $3, $5}' AllExome_sorted_as_bam.bed > fixed_for_vardict.bed", "description": "Example of fixing bed file"
})


#------------------------------------------------------------------------------------------------------------------
#Python commands
commands["Python"].append({
    "command": "len(my_list)", "description": "Get the length of a list"
})

commands["Python"].append({
    "command": "python /mnt/storage2/sequencing/software/WES+WTS/befundGen.py E-Nummer LibID WES LibID Normal Laufordner WES Laufordner WTS LibID WTS", "description": "Befund generation combined WES + WTS"
})


#------------------------------------------------------------------------------------------------------------------
#Conda commands
commands["Conda"].append({
    "command": "conda activate env", "description": "Activate a conda enviroment"
})

#------------------------------------------------------------------------------------------------------------------
#Git commands
commands["Git"].append({
    "command": "git commit -m 'description of change'", "description": "Commit changes on file/folder"
})

commands["Git"].append({
    "command": "git push origin master | git push -u origin main", "description": "Upload changes in the gitlab"
})

commands["Git"].append({
    "command": "git remote remove origin", "description": "remove existing origin in repository"
})

#------------------------------------------------------------------------------------------------------------------
#R commands
commands["R"].append({
    "command": "head(df)", "description": "View first few rows of a dataframe"
})

commands["R"].append({
    "command": "df[df == 0] <- NA", "description": "Transform all values equal to X into NA in data frame"
})

commands["R"].append({
    "command": "df <- df[!apply(is.na(df), 1, all), ]", "description": "Remove rows where all the elements are NA"
})

commands["R"].append({
    "command": "df[is.na(df)] <- """, "description": "Replace all NA values in a data frame with empty strings """
})


#------------------------------------------------------------------------------------------------------------------
#Snakemake commands:
commands["Snakemake"].append({
    "command": "snakemake --dag | dot -Tpdf > dag.pdf", 
    "description": "Create a workflow DAG diagram"
})

commands["Snakemake"].append({
    "command": "snakemake -s /mnt/storage2/sequencing/software/WES/snakemake_pipeline/Snakefile --configfile /mnt/storage2/sequencing/software/WES/snakemake_pipeline/default_wes_config.yaml --cores 64 --resources fpga=1 -p -k --use-conda --conda-frontend conda", 
    "description": "RUN WES folder analysis"
})

commands["Snakemake"].append({
    "command": "snakemake -s /mnt/storage2/sequencing/software/WTS/Snakefile --configfile /mnt/storage2/sequencing/software/WTS/wts_config.yaml --cores 64 -p --use-conda --conda-frontend conda", 
    "description": "RUN WES folder analysis"
})

commands["Snakemake"].append({
    "command": "--rerun-triggers mtime", 
    "description": "rerun workflow by time updated files"
})

commands["Snakemake"].append({
    "command": "--rerun-incomplete", 
    "description": "rerun workflow incompleted jobs"
})

commands["Snakemake"].append({
    "command": "--keep-going", 
    "description": "Keep running jobs even some rules failed"
})

commands["Snakemake"].append({
    "command": "--until", 
    "description": "Run jobs until a given rule"
})

commands["Snakemake"].append({
    "command": "snakemake -s Scripts/Snakefile --configfile Scripts/stranded_config.yaml --jobs 10 --cores 80 --use-conda --conda-frontend conda --until", 
    "description": "example snakemake run"
})

# Check structure by printing
for category, cmd_list in commands.items():
    print(f"Category: {category}")
    for cmd in cmd_list:
        print(f" - {cmd['command']}: {cmd['description']}")


# Start building the HTML ---------------------------------------------------------------------------------------------------------------
html_content = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Programming Commands Cheat Sheet</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #000000;
      margin: 0;
      padding: 0;
    }
    .window {
      width: 800px;
      height: 300px;
      background: #fff;
      border: 2px solid #333;
      border-radius: 10px;
      position: absolute;
      box-shadow: 4px 4px 15px rgba(0,0,0,0.2);
      user-select: text;
      display: flex;
      flex-direction: column;
    }
    .header {
      background: #2c3e50;
      color: white;
      padding: 10px;
      border-radius: 8px 8px 0 0;
      cursor: move;
      user-select: none;
      font-weight: bold;
    }
    .content {
      padding: 10px;
      overflow-y: auto;
      height: 100%;
    }
    code {
      background: #eee;
      padding: 2px 4px;
      border-radius: 3px;
      font-family: monospace;
    }
    ul {
      padding-left: 20px;
      margin: 0;
    }
    li {
      margin-bottom: 8px;
      line-height: 1.4em;
    }
  </style>
</head>
<body>
"""

# Add draggable divs for each category
offset_x = 50
offset_y = 50

ordered_categories = ["Linux", "Python","Conda","Git", "R", "Snakemake"]

for i, category in enumerate(ordered_categories):
    cmd_list = commands[category]
    top = offset_y + i * 60
    left = offset_x + i * 30

    html_content += f"""
    <div class="window" style="top: {top}px; left: {left}px;" id="win{i}">
      <div class="header">{category}</div>
      <div class="content">
        <ul>
    """
    for cmd in cmd_list:
        html_content += f"<li><code>{cmd['command']}</code> – {cmd['description']}</li>\n"
    html_content += "</ul></div></div>\n"

# Add JavaScript for dragging
html_content += """
<script>
  document.querySelectorAll('.window').forEach(win => {
    const header = win.querySelector('.header');
    let isDragging = false;
    let offsetX = 0, offsetY = 0;

    header.addEventListener('mousedown', e => {
      isDragging = true;
      offsetX = e.clientX - win.offsetLeft;
      offsetY = e.clientY - win.offsetTop;
      document.body.style.userSelect = 'none';
    });

    document.addEventListener('mousemove', e => {
      if (!isDragging) return;
      win.style.left = (e.clientX - offsetX) + 'px';
      win.style.top = (e.clientY - offsetY) + 'px';
    });

    document.addEventListener('mouseup', () => {
      isDragging = false;
      document.body.style.userSelect = '';
    });
  });
</script>
"""

# Timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
html_content += f"""
<div style="position: fixed; bottom: 10px; right: 10px; color: white; font-size: 12px;">
  Generated by Alejandro Pallares (PhD): {timestamp}
</div>
</body>
</html>
"""

# Save to file
with open("commands.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ Fixed HTML generated: commands.html")