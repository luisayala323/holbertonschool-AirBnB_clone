# Learning Objectives

    - What is HTML
    - How to create an HTML page
    - What is a markup language
    - What is the DOM
    - What is an element / tag
    - What is an attribute
    - How does the browser load a webpage
    - What is CSS
    - How to add style to an element
    - What is a class
    - What is a selector
    - How to compute CSS Specificity Value
    - What are Box properties in CSS

1.  HTML stands for Hypertext Markup Language. It is the standard markup language used to create and structure the content of web pages. HTML uses various tags and elements to define the structure, text, images, links, and other media elements within a webpage.

2.  To create an HTML page, you need a simple text editor like Notepad (Windows) or TextEdit (Mac). Follow these steps:
    - Open a text editor.
    - Create a new file and save it with a .html extension.
    - Add <!DOCTYPE html>.
    - Build the structure using <html>, <head>, and <body>.
    - Inside <head>, add <title> for the webpage's title.
    - In <body>, add content with HTML elements.
    - Save and view in a web browser.

Here's a simple example of an HTML page:

    <!DOCTYPE html>
    <html>
    <head>
    <title>My First Webpage</title>
    </head>
    <body>
    <h1>Hello, World!</h1>
    <p>This is my first webpage.</p>
    </body>
    </html>

3.  Markup language uses tags or codes to annotate a document's structure and content. HTML is a prime example, defining the structure and content of webpages for web browsers to interpret and display.

4.  The DOM (Document Object Model) is a browser's programming interface for dynamically modifying web pages using JavaScript. It represents the document's structure as a tree of objects, enabling developers to access and change content and styles in real-time.

5.  In HTML, an element (also known as a tag) is a fundamental building block that defines the structure and content of a document. Elements are represented by opening and closing tags, which enclose the content they describe.

6.  HTML attributes provide additional information about an element. They are specified within the opening tag of an element and consist of a name and a value, separated by an equal sign. Attributes modify the behavior or appearance of an element. For example, the src attribute in an <img> tag specifies the image's source URL.

7.  The browser loads a webpage by:

    Parsing the URL and finding the IP address.
    Sending an HTTP request to the web server.
    Receiving and rendering the HTML content.
    Downloading additional resources like images and scripts.
    Applying styles and executing JavaScript.
    Completing the page load for user interaction.

8.  CSS stands for Cascading Style Sheets. It is a stylesheet language used to control the presentation and layout of HTML documents. With CSS, you can apply styles such as colors, fonts, margins, padding, and positioning to elements on a webpage. CSS allows you to separate the document's content (HTML) from its presentation (styling), making it easier to maintain and update the design.

9.  You can add styles to an element using CSS. There are multiple ways to apply styles, but the most common is by using the style attribute directly in the HTML element.

Example:

    <p style="color: blue; font-size: 16px;">This is a styled paragraph.</p>

10. A class in CSS is a reusable identifier that allows you to apply styles to multiple elements without having to repeat the styles for each element individually. You can assign a class to an HTML element using the class attribute. Then, in your CSS stylesheet, you define the styles for that class, and any element with that class will inherit those styles.

11. In CSS, a selector is a pattern that is used to select and target specific HTML elements to apply styles. Selectors can be based on element names, class names, IDs, attributes, and more. CSS rules consist of selectors followed by curly braces {} that contain the styles to be applied to the selected elements.

Example:

    p {
    color: blue;
    }

12. To compute CSS specificity:

    Count ID selectors (1 per ID).
    Count class selectors, attribute selectors, and pseudo-classes (1 per class, attribute, or pseudo-class).
    Count element selectors and pseudo-elements (1 per element or pseudo-element).
    For inline styles, add 1000 to the specificity value.
