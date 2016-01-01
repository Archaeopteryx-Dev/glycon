from django.template.loader import render_to_string


def summary_page(request, viewname):
    return


def summary_block_html(block):
    return render_to_string("summaryblock.html", context={"block": block})