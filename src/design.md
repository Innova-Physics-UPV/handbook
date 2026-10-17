# How we design

## Lifecycle of a deliverable

Every deliverable, from a circuit board to a complete machine, passes through the same stages.

1. **Define.** Requirements and acceptance criteria are written before design starts. They state what will be measured to show that the deliverable works.
2. **Design and simulate.** The design is developed in the repository, with its calculations and simulations.
3. **Review.** The department lead or a member Qualified in the area reviews the design before anything is ordered or built. Designs involving high voltage, vacuum or the beam also pass a safety review.
4. **Build.** The deliverable is built as designed, and every deviation is recorded.
5. **Test.** The deliverable is measured against the acceptance criteria written at the start.
6. **Release.** Design files, test results and documentation are published.

A machine built for users passes one more stage before handover. It measures reference samples only; the university's radiation protection and occupational safety services check its dose rate and its electrical safety; and a written agreement fixes ownership, maintenance, training and responsibility for safety. From then on, the users decide every measurement.

## Tasks and pull requests

All work is tracked as tasks in our GitHub organisation. Every task has an associated pull request, opened early as a draft and merged after review. A task is done when its pull request is merged; work that is not in the repository is not done.

When accepted work changes how a machine is built or operated, the public design documentation is updated as part of the same task.

## Design Decision Records

Every decision that constrains the design is recorded in a short Design Decision Record: the decision, the alternatives considered and the reason.

## Machine parameters

The parameters of each machine live in a single parameter table. Drawings, simulations and documents refer to it, and changing it takes a Design Decision Record.

## Reports and notes

Results are written up in two numbered series, set in the team's LaTeX class: INNOVA-REP for reports and papers, INNOVA-TN for technical notes. A simulation report states the tool and its version, every input value and the method, so that another person can reproduce the result; large model files stay on the team's workstations. Before a document is released, a member who is not among its authors reads and checks it. Released documents are published openly, with a DOI, under CC BY 4.0.
