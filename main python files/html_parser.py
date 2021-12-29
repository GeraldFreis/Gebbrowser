
from os import defpath, write
from typing import Literal
import urllib
from urllib.request import urlopen
try:
    from bs4 import BeautifulSoup
except Exception:
    pass

"""Globals"""
base_url = "http://www.blankwebsite.com/"
google_url = "https://www.google.com"


"""Functions"""
def checkingelements(textline):  # function to check whether or not an element is a html element and to add the element to a dictionary if it is
    # if statements to determine whether or not to add the data in the dictionary
    html_tag_list = ("<a>", "<address>", "<area>", "<article>", "<aside>", "<audio>", "<b>",
    "<base>", "<bdo>", "<blockquote>", "<body>", "<br />", "<button>", "<canvas>",
    "<caption>", "<cite>", "<code>", "<col>", "<colgroup>", "<command>", "<datagrid>", 
    "<datalist>", "<dd>", "<del>", "<details>", "<dfn>", "<dir>", "<div>", "<dl>",
    "<dt>", "<em>", "<embed>", "<fieldset>", "<figcaption>", "<figure>", "<font>",
    "<footer>", "<form>", "<frame>", "<frameset>", "<h1>", "<h2>", "<h3>", "<h4>", "<h5>",
    "<h6>", "<head>", "<header>", "<hgroup>", "<hr />", "<html>", "<i>", "<iframe>",
    "<img>", "<input>", "<ins>", "<kbd>", "<keygen>", "<label>", "<legend>",
    "<li>", "<link>", "<map>", "<mark>", "<menu>", "<meta>", "<meter>", "<nav>", "<noscript>", "<object>",
    "<ol>", "<optgroup>", "<option>", "<output>", "<p>", "<param>", "<pre>", "<progress>", "<q>",
    "<rp>", "<rt>", "<ruby>", "<s>", "<samp>", "<script>", "<section>", "<select>", "<source>", "<span>", "<strong>", "<style>", "<sub>", "<sup>", "<table>", "<tbody>", "<td>", "<textarea>", "<tfoot>", "<th>", "<thead>", "<time>", "<title>", "<tr>", "<track>", "<u>", "<ul>", "<var>", "<video>", "<wbr>" )

    for tag in html_tag_list:
        if tag in textline:
            print(textline)


"""Parser to find the main html elements"""
class HtmlParser():
    def __init__(self, urltoparse):
        self.url_to_parse = urltoparse

        with urlopen(self.url_to_parse) as f:

            self.text = str(f.read())
            self.temptext = open("urltext.html", "w")
            self.temptext.write(self.text)
            self.temptext.close()

            self.html_doc = open("urltext.html", "r")
            self.soup = BeautifulSoup(self.html_doc, 'html.parser')
            self.html_doc_write = open("urltext.html", "w")
            self.html_doc_write.write(self.soup.prettify())

            """Iterating through the html doc and printing it to a temporary text file, once text file exists it is iterated through and produces a """
            self.temporary_text_file_writeable = open("temphtml.txt", "w")
            self.temporary_text_file_writeable.write(self.soup.prettify())


        self.temporary_text_file_readable = open("temphtml.txt", "r")
        self.html_doc.close()
        self.html_doc_write.close()
        self.temporary_text_file_writeable.close()
        self.temporary_text_file_readable.close()

    def returningtitle(self):
        """Returning the title"""
        return self.soup.title.string

    
    def iterthroughfiles(self):
        doc = open("temphtml.txt", "r")
        for row in doc:
            checkingelements(textline=row)

htmlparser = HtmlParser(base_url)
htmlparser.iterthroughfiles()

