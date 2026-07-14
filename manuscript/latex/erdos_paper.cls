\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{erdos_paper}[2026/07/14 Custom class for Erdos Problem 470 manuscript]

% Inherit from standard article
\LoadClass[12pt]{article}

% Required packages
\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage{amsthm}
\RequirePackage{xcolor}
\RequirePackage{hyperref}
\RequirePackage{booktabs}
\RequirePackage{geometry}
\RequirePackage{fancyhdr}
\RequirePackage{datetime}
\RequirePackage{longtable}
\RequirePackage{calc}
\RequirePackage{array}
\RequirePackage{tikz}

% Tight list for Pandoc
\providecommand{\tightlist}{%
  \setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}

% Colors
\definecolor{matmaila}{HTML}{E8E0C5}
\pagecolor{matmaila}

% Page Geometry
\geometry{margin=1.2in}

% Circled page number command
\newcommand{\circledpage}{%
  \begin{tikzpicture}[baseline=(char.base)]
    \node[draw, circle, inner sep=4pt, line width=0.5pt, text=black] (char) {\thepage};
  \end{tikzpicture}%
}

% Header/Footer styling
\fancypagestyle{plain}{
  \fancyhf{}
  \renewcommand{\headrulewidth}{0pt}
  \fancyfoot[C]{\circledpage}
}
\pagestyle{plain}
\setcounter{secnumdepth}{0}
\setcounter{tocdepth}{3}

% Hyperref setup for Table of Contents
\hypersetup{
    colorlinks=true,
    linkcolor=black,
    filecolor=magenta,      
    urlcolor=blue,
    pdftitle={Erdos Problem 470},
    pdfpagemode=FullScreen,
}

% Custom Title Maketitle command
\renewcommand{\maketitle}{
    \begin{center}
        \vspace*{2em}
        {\Large \bfseries \@title \par}
        \vspace{1.5em}
        {\large \@author \par}
        \vspace{0.5em}
        {\normalsize \textit{India} \par}
    \end{center}
    \vspace{2em}
}

% Custom Abstract environment
\renewenvironment{abstract}{
    \noindent\makebox[\linewidth]{\rule{\textwidth}{0.4pt}}
    \vspace{0.5em}
    \noindent\textbf{Abstract}\par
    \vspace{0.5em}
    \noindent\ignorespaces
}{
    \vspace{0.5em}
    \noindent\makebox[\linewidth]{\rule{\textwidth}{0.4pt}}
    \vspace{2em}
}

\endinput
