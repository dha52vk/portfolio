import re

with open("exercise_list.html", "r", encoding="utf-8") as f:
    content = f.read()

new_section = """<!-- Footer Stats / Progress Section -->
<section class="mt-section-gap bg-surface-container-high p-8 rounded-2xl flex flex-wrap gap-8 items-center justify-between border border-outline-variant">
<div class="flex items-center gap-4">
<div class="w-16 h-16 rounded-full border-4 border-primary border-t-transparent animate-spin-slow"></div>
<div>
<h4 class="font-headline-sm text-headline-sm text-primary">Trạng thái hoàn thành</h4>
<p class="text-on-surface-variant font-body-md">Tất cả 6 bài tập đã được hệ thống hóa.</p>
</div>
</div>
<div class="flex gap-4">
<button onclick="window.open('fullreport.pdf', '_blank')" class="bg-primary text-white px-8 py-3 rounded-full font-label-md text-label-md flex items-center gap-2 hover:opacity-90 transition-opacity">
<span class="material-symbols-outlined" data-icon="file_download">file_download</span> Tải báo cáo tổng hợp
                    </button>
<button class="bg-white text-primary border border-primary px-8 py-3 rounded-full font-label-md text-label-md hover:bg-surface-container transition-colors">
                        Xem Gallery
                    </button>
</div>
</section>
"""

content = re.sub(r'(</div>\s*</main>)', lambda m: new_section + m.group(1), content)

with open("exercise_list.html", "w", encoding="utf-8") as f:
    f.write(content)
