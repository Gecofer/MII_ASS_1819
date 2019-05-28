\LoadClass[11pt]{article}
\usepackage{eurosym}
\usepackage[utf8]{inputenc}
\usepackage[spanish]{babel}
\usepackage{titlesec}
\usepackage{titling}
\usepackage{color}
\usepackage{graphicx}
\usepackage{indentfirst}
\usepackage{float}
\usepackage{setspace} 
\usepackage{afterpage}
\usepackage{tabularx}
\usepackage{fancyhdr}
\usepackage[labelfont=bf,textfont=bf]{caption}
\usepackage[toc,page]{appendix}
\usepackage{subfigure}
\usepackage{url}
\usepackage{hyperref}
\usepackage{listings}
\usepackage{tikz}
\usepackage{listings}
\usepackage{verbatim}
\usepackage{xcolor}
\usepackage{color}
\usepackage{multicol}
\usepackage{xpatch}
\usepackage{filecontents}
\usepackage{nopageno}
\usepackage{pdfpages}
\usepackage{colortbl}
\usepackage{wrapfig}

\definecolor{verde}{rgb}{0,0.5,0}
\definecolor{mygray}{rgb}{0.5,0.5,0.5}
\definecolor{gris}{rgb}{0.15,0.15,0.15}
\definecolor{gray97}{gray}{.97}
\definecolor{gris1}{RGB}{220,220,220}

\usepackage[a4paper, margin=1.3in]{geometry}

% ----- Encabezado ----- %
\pagestyle{fancy}
\fancyhf{}
\lhead{Certificados Digitales: DNI Electrónico} % nombre de la práctica
\rhead{\thepage}
%\cfoot{} % quitar número de página del centro
%\rfoot{\thepage} % número de página a la derecha


% ----- Márgenes ----- %
% Define los márgenes
%\RequirePackage[a4paper, left = 1.18in, right = 1.35in, top = 1.18in, 
%               bottom = 0.79in]{geometry}

% Para establecer los márgenes de página


\newcommand{\MONTH}{%
  \ifcase\the\month
  \or Enero % 1
  \or Febrero % 2
  \or Marzo % 3
  \or Abril % 4
  \or Mayo % 5
  \or Junio % 6
  \or Julio % 7
  \or Agosto % 8
  \or Septiembre % 9
  \or Octubre % 10
  \or Noviembre % 11
  \or Diciembre % 12
  \fi}

% ----- Formato ----- %
% Formato párrafo
\parindent=0.49in
\parskip=6pt
%\onehalfspacing

% Configura secciones y variantes %
\renewcommand\section{\@startsection{section}{1}{\z@}%
                       {-18\p@ \@plus -4\p@ \@minus -4\p@}%
                       {12\p@ \@plus 4\p@ \@minus 4\p@}%
                       {\normalfont\large\bfseries\boldmath
                        \rightskip=\z@ \@plus 8em\pretolerance=10000 }}
                        
\renewcommand\subsection{\@startsection{subsection}{2}{\z@}%
                       {-18\p@ \@plus -4\p@ \@minus -4\p@}%
                       {8\p@ \@plus 4\p@ \@minus 4\p@}%
                       {\normalfont\normalsize\bfseries\boldmath
                        \rightskip=\z@ \@plus 8em\pretolerance=10000 }}
                        
\newcommand{\subsubsubsection}[1]{\paragraph{#1}\mbox{}\\}    

%\renewcommand\subsubsection{\@startsection{subsection}{3}{\z@}%
%                       {-18\p@ \@plus -4\p@ \@minus -4\p@}%
%                       {8\p@ \@plus 4\p@ \@minus 4\p@}%
%                       {\normalfont\normalsize\bfseries\boldmath
%                        \rightskip=\z@ \@plus 8em\pretolerance=10000 }}

\renewcommand\paragraph{\@startsection{paragraph}{4}{\z@}%
                       {-12\p@ \@plus -4\p@ \@minus -4\p@}%
                       {-0.5em \@plus -0.22em \@minus -0.1em}%
                       {\normalfont\normalsize\itshape}}

% ----- Código ----- %
% Para customizar el código 
\lstset{language=Java, %defina a linguagem usada no trabalho
              belowcaptionskip=1\baselineskip,
                breaklines=true,
                %frame=false,
                %xleftmargin=\parindent,
                showstringspaces=false,
                basicstyle=\footnotesize\ttfamily\color{purple!40!black},
                keywordstyle=\bfseries\color{blue},
                commentstyle=\itshape\color{green!40!black},
                identifierstyle=\color{black},
                stringstyle=\color{orange},
                numbers=left,
                backgroundcolor=\color{gray97},
                rulesepcolor=\color{black},
                rulesep=0pt,	
                numberstyle=\tiny\color{mygray}, 
            }


% ----- Referencias ----- %

%https://tex.stackexchange.com/questions/133749/how-to-cite-the-web-page-address-as-the-reference

%\usepackage[nottoc]{tocbibind}
%\usepackage[
%backend=biber,
%style=alphabetic,
%sorting=ynt
%]{biblatex}
%\addbibresource{references.bib} %Imports bibliography file

\usepackage{parskip} %Para eliminar la sangría
\usepackage{booktabs} 
\usepackage{tabulary}
\usepackage{bbding}
\usepackage{wasysym}
\usepackage{amssymb}% http://ctan.org/pkg/amssymb
\usepackage{pifont}% http://ctan.org/pkg/pifont
\newcommand{\cmark}{\ding{51}}%
\newcommand{\xmark}{\ding{55}}%
\usepackage{longtable}
\usepackage{multirow}
\usepackage{pdflscape}
%\usepackage{lscape}
%\usepackage[landscape]{geometry}