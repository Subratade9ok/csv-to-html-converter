#!/usr/bin/env python3
import sys


def csv_to_html(css,js,className):
    with open(sys.argv[1],'r') as csvfile:
      with open(sys.argv[2],'w+') as html:
        i = 0
        html.write('<html>\n\t<head>\n\t\t<title>Converted {} to {}</title>\n{}\n\t</head>\n<body>\n<table class="{}">\n'.format(sys.argv[1], sys.argv[2], css, className))
        for line in csvfile.readlines():
          data=line.split(',')
          if i == 0:
            html.write('<thead>\n')
          if i == 1:
            html.write('<tbody>\n')
          html.write('\t<tr>\n')
          if data[0]=='\n':
            pass
          else:
            print(str(data))
            for tr in data:
              if i == 0:
                html.write('\t\t<th scope="col">{}</th>\n'.format(tr.strip()))
              else:
                html.write('\t\t<td>{}</td>\n'.format(tr.strip()))
          html.write('\t</tr>\n')
          if i==0 :
            html.write('</thead>\n')
          i+=1
        html.write('</tbody>\n')
        html.write('\n{}'.format(js))
        html.write('</table>\n</body>\n</html>')
        html.close()
      csvfile.close()
  
  
  
  
  
css = '\t<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">'
className = 'table table-striped table-dark'
js = '\n<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>\n'
csv_to_html(css,js,className)    
print("Task Completed")
