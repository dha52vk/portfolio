import re

with open("exercise_list.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace button with anchor tag
content = content.replace(
    '''<button onclick="window.open('fullreport.pdf', '_blank')" class="bg-primary text-white px-8 py-3 rounded-full font-label-md text-label-md flex items-center gap-2 hover:opacity-90 transition-opacity">
<span class="material-symbols-outlined" data-icon="file_download">file_download</span> Tải báo cáo tổng hợp
                    </button>''',
    '''<a href="fullreport.pdf" download="fullreport.pdf" class="bg-primary text-white px-8 py-3 rounded-full font-label-md text-label-md flex items-center gap-2 hover:opacity-90 transition-opacity inline-flex">
<span class="material-symbols-outlined" data-icon="file_download">file_download</span> Tải báo cáo tổng hợp
                    </a>'''
)

# Remove duplicate comment
content = content.replace("<!-- Footer Stats / Progress Section -->\n<!-- Footer Stats / Progress Section -->", "<!-- Footer Stats / Progress Section -->")

with open("exercise_list.html", "w", encoding="utf-8") as f:
    f.write(content)
