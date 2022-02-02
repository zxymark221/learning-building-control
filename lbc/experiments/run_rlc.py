import logging

from lbc.experiments.runner import PolicyRunner, SCENARIO_DEFAULT
from lbc.experiments.runner import SCENARIO_TEST
from lbc.simulate import simulate


logger = logging.getLogger(__file__)


class RLCRunner(PolicyRunner):

    def run_policy(self, policy):
        loss, rollout, meta = simulate(
            policy=policy, scenario=self.scenario, batch_size=self.batch_size)
        return loss, rollout, meta


def main(**kwargs):
    runner = RLCRunner(**kwargs)
    runner.run()


if __name__ == "__main__":

    from lbc.experiments.runner import parser

    a = parser.parse_args()

    # Use the args to construct a full configuration for the experiment.
    config = {
        "name": f"RLC-{a.dr_program}",
        "policy_type": "RLC",
        "dr_program": a.dr_program,
        "batch_size": a.batch_size,
        "scenario_config": SCENARIO_TEST if a.dry_run else SCENARIO_DEFAULT,
        "policy_config": {},
        "training": False,
        "dry_run": a.dry_run
    }
    print("ARGS:", config)

    _ = main(**config)