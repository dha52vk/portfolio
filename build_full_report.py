import re
import os

root_dir = r"d:\dha52\Documents\Github\portfolio"

with open(os.path.join(root_dir, "index.html"), "r", encoding="utf-8") as f:
    index_html = f.read()

# Extract head
head_match = re.search(r'(<head>.*?</head>)', index_html, re.DOTALL)
head = head_match.group(1) if head_match else ""

# Add smooth scrolling
head = head.replace('<style>', '<style>\n        html { scroll-behavior: smooth; }\n')

# Extract body attributes and top nav
body_match = re.search(r'(<body.*?>)', index_html, re.DOTALL)
body_tag = body_match.group(1) if body_match else '<body class="bg-background text-on-surface overflow-x-hidden">'

top_nav_match = re.search(r'(<!-- Top Navigation Bar -->.*?</header>)', index_html, re.DOTALL)
top_nav = top_nav_match.group(1) if top_nav_match else ""

# Fix links in top_nav to point to sections in full report
top_nav = re.sub(r'href="index\.html(#about)?"', 'href="#top"', top_nav)
top_nav = re.sub(r'href="exercise_list\.html"', 'href="#exercises"', top_nav)
top_nav = re.sub(r'<!-- Mobile Toggle -->.*?<button id="mobile-menu-btn".*?</button>', '', top_nav, flags=re.DOTALL)

# Extract index main content
index_main_match = re.search(r'<main.*?>(.*?)</main>', index_html, re.DOTALL)
index_main_content = index_main_match.group(1) if index_main_match else ""

# Extract footer
footer_match = re.search(r'(<footer.*?>.*?</footer>)', index_html, re.DOTALL)
footer = footer_match.group(1) if footer_match else ""
footer = footer.replace('lg:ml-64', '')

# Build full report
full_html = f"""<!DOCTYPE html>
<html lang="vi">
{head}
{body_tag}
<div id="top"></div>
{top_nav}

<main class="flex-1 pt-16 min-h-screen flex flex-col">
    <!-- HOMEPAGE CONTENT -->
    <div class="mb-24">
        {index_main_content}
    </div>
    
    <div id="exercises" class="border-t-[8px] border-surface-variant mb-24"></div>
"""

exercises = ["exercise1.html", "exercise2.html", "exercise3.html", "exercise4.html", "exercise5.html", "exercise6.html"]

for ex_file in exercises:
    ex_path = os.path.join(root_dir, "exercises", ex_file)
    with open(ex_path, "r", encoding="utf-8") as f:
        ex_content = f.read()
        
    # Extract inner content, stripping the Navigation Actions
    # First split by <!-- Navigation Actions --> if it exists
    parts = ex_content.split('<!-- Navigation Actions -->')
    if len(parts) > 1:
        # Get everything before it inside the main container
        main_content = parts[0]
        # remove the top parts (header and breadcrumbs)
        # Find where the actual content starts. Let's just find <div class="max-w-[1200px]...">
        inner_match = re.search(r'<div class="max-w-\[1200px\].*?>(.*)', main_content, re.DOTALL)
        ex_inner = inner_match.group(1) if inner_match else main_content
    else:
        inner_match = re.search(r'<div class="max-w-\[1200px\].*?>(.*)</div>\s*</main>', ex_content, re.DOTALL)
        ex_inner = inner_match.group(1) if inner_match else ""
    
    # Remove breadcrumbs block
    ex_inner = re.sub(r'<!-- Breadcrumbs -->.*?</nav>', '', ex_inner, flags=re.DOTALL)
    
    # Remove the header "mb-12" entirely? No, keep the H1.
    # Actually just remove the <nav> Breadcrumbs entirely.
    ex_inner = re.sub(r'<nav class="flex items-center gap-2 mb-8 text-on-surface-variant">.*?</nav>', '', ex_inner, flags=re.DOTALL)
    
    # Fix paths
    ex_inner = ex_inner.replace("../assets/", "assets/")
    ex_inner = ex_inner.replace("../index.html", "index.html")
    ex_inner = ex_inner.replace("../exercise_list.html", "exercise_list.html")
    
    ex_id = ex_file.replace(".html", "")
    
    full_html += f"""
    <!-- {ex_id.upper()} -->
    <section id="{ex_id}" class="max-w-[1200px] w-full mx-auto px-margin-mobile md:px-gutter py-stack-lg min-w-0">
        {ex_inner}
    </section>
    
    <div class="border-t border-outline-variant/30 my-16 mx-margin-mobile md:mx-gutter"></div>
"""

full_html += f"""
</main>
{footer}
</body>
</html>
"""

out_path = os.path.join(root_dir, "full_report.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"Created {out_path}")
