# NSCI 395 — Introduction to Computational Neuroscience

Student-facing course materials for NSCI 395 at Hope College, Fall 2026.

Materials will be released incrementally as Jupyter Notebooks. 
Live notebooks will be published before class for students to review ahead of time; in class, the live notebook will be filled out by the instructor with students working along in their own copies.
Completed notebooks are published as
separate files after class.

Use the course link in Moodle to open or update these materials in JupyterHub.
See Moodle for deadlines, assignment instructions,
grades, and course announcements.

## What is here

| Folder | What it holds |
| --- | --- |
| `activities/` | In-class workspaces: orientation, the Git routine, debugging, studios |
| `syllabus/` | A link to the syllabus and schedule, which live in one Google Doc |
| `resources/` | Reference sheets you will use all semester: Python quick reference, debugging, figure and claim checklists, optional readings |
| `notebooks/` | Lecture notebooks, once released. `live/` before class, `completed/` after |
| `data/` | Small course datasets, with their source and licence notes |

Folders appear as material is released. If one is missing, it has not been
published yet.

## What the file names mean

Every notebook and assignment starts with a letter code. The letter says what
kind of thing it is; the number says where it sits in that sequence.

| Code | What it is | Range |
| --- | --- | --- |
| `P` | Python foundations | P00-P12 |
| `M` | Modelling single neurons | M01-M06 |
| `D` | Real spike data | D00-D05 |
| `C` | Circuits | C01-C03 |
| `POP` | Population analysis | POP01-POP02 |
| `S` | Model choice and defensible claims | S01-S02 |
| `A` | Activities: in-class workspaces | A00-A09 |
| `G` | Guided assignments | G01-G04 |
| `I` | Individual investigations | I01-I02 |
| `Q` | In-class quizzes | Q01-Q03 |
| `CC` | Quick concept checks, weekly | CC01-CC15 |
| `PM`, `PD` | Semester project options: modelling, data | PM1-PM4, PD1-PD4 |

Lecture notebooks come in two versions. `_LIVE` is the scaffolded one you get
before class and work in during it. `_COMPLETED` is the canonical version
released afterwards; compare, do not copy.

The numbers are not always contiguous. P02, P10 and P12 exist as optional
reference notebooks rather than scheduled classes, so the taught sequence steps
over them.


## Working in JupyterHub

Use the single editable folder `~/NSCI395/course-materials`. Before the class
Git lesson, newly released paths arrive automatically and existing work is not
overwritten. After running the instructor-provided `course-git-setup` command,
commit current work and run `course-sync` before class to merge new releases.

The Git-backed folder uses two standard remotes:

- `upstream` is this public, instructor-maintained source;
- `origin` is the student's private semester repository.

Use the JupyterLab Git sidebar to review changes, stage, commit, and push to the
private `origin`. The read-only `~/NSCI395/course-materials-readonly` path is an
always-current reference and recovery copy.

No graded work should be submitted to this repository. Individual assignments
and team projects use separate private repositories.

## License

Except where a file includes a different source or license notice, original
course text and notebooks are licensed under the
[Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
Third-party datasets and other incorporated materials remain subject to their
respective source and license notices.
