# This Python file uses the following encoding: utf-8

import io
from contextlib import redirect_stderr
from unittest import TestCase

from panflute import convert_text

import pandoc_beamer_arrow


def conversion(markdown, fmt="markdown"):
    doc = convert_text(markdown, standalone=True)
    doc.format = fmt
    pandoc_beamer_arrow.main(doc)
    return doc


class NodeTest(TestCase):
    def test_simple(self):
        doc = conversion("[**abc**]{.beamer-arrow-node #id1}", fmt="beamer")
        text = convert_text(
            doc,
            input_format="panflute",
            output_format="latex",
            extra_args=["--wrap=none"],
        )
        self.assertEqual(
            text, r"\tikz[baseline]{{\node[anchor=base] (id1) {\textbf{abc}};}}"
        )

    def test_color(self):
        doc = conversion('[**abc**]{.beamer-arrow-node #id1 color="red"}', fmt="beamer")
        text = convert_text(
            doc,
            input_format="panflute",
            output_format="latex",
            extra_args=["--wrap=none"],
        )
        self.assertEqual(
            text,
            r"\tikz[baseline]{{\node[anchor=base,fill=red] (id1) {\textbf{abc}};}}",
        )

    def test_bad_color(self):
        stream = io.StringIO()
        with redirect_stderr(stream):
            doc = conversion(
                '[**abc**]{.beamer-arrow-node #id1 color="unknown"}', fmt="beamer"
            )
            text = convert_text(
                doc,
                input_format="panflute",
                output_format="latex",
                extra_args=["--wrap=none"],
            )
            self.assertEqual(
                text, r"\tikz[baseline]{{\node[anchor=base] (id1) {\textbf{abc}};}}"
            )
            self.assertEqual(
                stream.getvalue(),
                "pandoc-beamer-arrow: color 'unknown' is not correct\n",
            )

    def test_from(self):
        doc = conversion('[**abc**]{.beamer-arrow-node #id1 from="2"}', fmt="beamer")
        text = convert_text(
            doc,
            input_format="panflute",
            output_format="latex",
            extra_args=["--wrap=none"],
        )
        self.assertEqual(
            text,
            r"\tikz[baseline]{\only<2->{\node[anchor=base] (id1) {\textbf{abc}};}}",
        )

    def test_bad_from(self):
        stream = io.StringIO()
        with redirect_stderr(stream):
            doc = conversion(
                '[**abc**]{.beamer-arrow-node #id1 from="bad"}', fmt="beamer"
            )
            text = convert_text(
                doc,
                input_format="panflute",
                output_format="latex",
                extra_args=["--wrap=none"],
            )
            self.assertEqual(
                text, r"\tikz[baseline]{{\node[anchor=base] (id1) {\textbf{abc}};}}"
            )
            self.assertEqual(
                stream.getvalue(),
                "pandoc-beamer-arrow: from value 'bad' is not correct\n",
            )

    def test_to(self):
        doc = conversion('[**abc**]{.beamer-arrow-node #id1 to="2"}', fmt="beamer")
        text = convert_text(
            doc,
            input_format="panflute",
            output_format="latex",
            extra_args=["--wrap=none"],
        )
        self.assertEqual(
            text,
            r"\tikz[baseline]{\only<-2>{\node[anchor=base] (id1) {\textbf{abc}};}}",
        )

    def test_bad_to(self):
        stream = io.StringIO()
        with redirect_stderr(stream):
            doc = conversion(
                '[**abc**]{.beamer-arrow-node #id1 to="bad"}', fmt="beamer"
            )
            text = convert_text(
                doc,
                input_format="panflute",
                output_format="latex",
                extra_args=["--wrap=none"],
            )
            self.assertEqual(
                text, r"\tikz[baseline]{{\node[anchor=base] (id1) {\textbf{abc}};}}"
            )
            self.assertEqual(
                stream.getvalue(),
                "pandoc-beamer-arrow: to value 'bad' is not correct\n",
            )

    def test_incompatible_from_to(self):
        stream = io.StringIO()
        with redirect_stderr(stream):
            doc = conversion(
                '[**abc**]{.beamer-arrow-node #id1 from="2" to="1"}', fmt="beamer"
            )
            text = convert_text(
                doc,
                input_format="panflute",
                output_format="latex",
                extra_args=["--wrap=none"],
            )
            self.assertEqual(
                text, r"\tikz[baseline]{{\node[anchor=base] (id1) {\textbf{abc}};}}"
            )
            self.assertEqual(
                stream.getvalue(),
                "pandoc-beamer-arrow: from value '2' and  to value '1' are incompatible\n",
            )


class ArrowTest(TestCase):
    def test_simple(self):
        doc = conversion(
            '[**abc**]{.beamer-arrow-edge src="id1" dest="id2"}', fmt="beamer"
        )
        text = convert_text(
            doc,
            input_format="panflute",
            output_format="latex",
            extra_args=["--wrap=none"],
        )
        self.assertEqual(
            text,
            r"\begin{tikzpicture}"
            r"[overlay]\path[->] (id1) edge [] (id2);"
            r"\end{tikzpicture}",
        )

    def test_angle_src(self):
        doc = conversion(
            '[**abc**]{.beamer-arrow-edge src="id1" dest="id2" angle_src="90"}',
            fmt="beamer",
        )
        text = convert_text(
            doc,
            input_format="panflute",
            output_format="latex",
            extra_args=["--wrap=none"],
        )
        self.assertEqual(
            text,
            r"\begin{tikzpicture}"
            r"[overlay]\path[->] (id1) edge [in=90] (id2);"
            r"\end{tikzpicture}",
        )

    def test_bad_angle_src(self):
        stream = io.StringIO()
        with redirect_stderr(stream):
            doc = conversion(
                '[**abc**]{.beamer-arrow-edge src="id1" dest="id2" angle_src="bad"}',
                fmt="beamer",
            )
            text = convert_text(
                doc,
                input_format="panflute",
                output_format="latex",
                extra_args=["--wrap=none"],
            )
            self.assertEqual(
                text,
                r"\begin{tikzpicture}"
                r"[overlay]\path[->] (id1) edge [] (id2);"
                r"\end{tikzpicture}",
            )
            self.assertEqual(
                stream.getvalue(),
                "pandoc-beamer-arrow: angle_src 'bad' is not correct\n",
            )

    def test_angle_dest(self):
        doc = conversion(
            '[**abc**]{.beamer-arrow-edge src="id1" dest="id2" angle_dest="90"}',
            fmt="beamer",
        )
        text = convert_text(
            doc,
            input_format="panflute",
            output_format="latex",
            extra_args=["--wrap=none"],
        )
        self.assertEqual(
            text,
            r"\begin{tikzpicture}"
            r"[overlay]\path[->] (id1) edge [out=90] (id2);"
            r"\end{tikzpicture}",
        )

    def test_bad_angle_dest(self):
        stream = io.StringIO()
        with redirect_stderr(stream):
            doc = conversion(
                '[**abc**]{.beamer-arrow-edge src="id1" dest="id2" angle_dest="bad"}',
                fmt="beamer",
            )
            text = convert_text(
                doc,
                input_format="panflute",
                output_format="latex",
                extra_args=["--wrap=none"],
            )
            self.assertEqual(
                text,
                r"\begin{tikzpicture}"
                r"[overlay]\path[->] (id1) edge [] (id2);"
                r"\end{tikzpicture}",
            )
            self.assertEqual(
                stream.getvalue(),
                "pandoc-beamer-arrow: angle_dest 'bad' is not correct\n",
            )

    def test_color(self):
        doc = conversion(
            '[**abc**]{.beamer-arrow-edge src="id1" dest="id2" color="red"}',
            fmt="beamer",
        )
        text = convert_text(
            doc,
            input_format="panflute",
            output_format="latex",
            extra_args=["--wrap=none"],
        )
        self.assertEqual(
            text,
            r"\begin{tikzpicture}"
            r"[overlay]\path[->,red] (id1) edge [] (id2);"
            r"\end{tikzpicture}",
        )

    def test_linewidth(self):
        doc = conversion(
            '[**abc**]{.beamer-arrow-edge src="id1" dest="id2" linewidth="3"}',
            fmt="beamer",
        )
        text = convert_text(
            doc,
            input_format="panflute",
            output_format="latex",
            extra_args=["--wrap=none"],
        )
        self.assertEqual(
            text,
            r"\begin{tikzpicture}"
            r"[overlay]\path[->,line width=3pt] (id1) edge [] (id2);"
            r"\end{tikzpicture}",
        )

    def test_bad_linewidth(self):
        stream = io.StringIO()
        with redirect_stderr(stream):
            doc = conversion(
                '[**abc**]{.beamer-arrow-edge src="id1" dest="id2" linewidth="bad"}',
                fmt="beamer",
            )
            text = convert_text(
                doc,
                input_format="panflute",
                output_format="latex",
                extra_args=["--wrap=none"],
            )
            self.assertEqual(
                text,
                r"\begin{tikzpicture}"
                r"[overlay]\path[->] (id1) edge [] (id2);"
                r"\end{tikzpicture}",
            )
            self.assertEqual(
                stream.getvalue(),
                "pandoc-beamer-arrow: linewidth 'bad' is not correct\n",
            )

    def test_range(self):
        doc = conversion(
            '[**abc**]{.beamer-arrow-edge src="id1" dest="id2" to="3" from="2"}',
            fmt="beamer",
        )
        text = convert_text(
            doc,
            input_format="panflute",
            output_format="latex",
            extra_args=["--wrap=none"],
        )
        self.assertEqual(
            text,
            r"\begin{tikzpicture}[overlay]\path[->]<2-3> (id1) edge [] (id2);\end{"
            r"tikzpicture}",
        )
