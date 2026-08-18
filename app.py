from agent import TruthLensAgent
from verifier import Verifier


def display_result(data):

    result = data["result"]
    citations = data["citations"]

    print("\n" + "=" * 60)
    print("TRUTHLENS RESULT")
    print("=" * 60)

    print(f"\nCLAIM:")
    print(result.claim)

    print(f"\nVERDICT:")
    print(result.verdict)

    print(f"\nCONFIDENCE:")
    print(f"{result.confidence}%")

    print(f"\nSUMMARY:")
    print(result.summary)

    print(f"\nREASONING:")
    print(result.reasoning)

    print("\nEVIDENCE:")

    for evidence in result.evidence:

        status = (
            "SUPPORTS"
            if evidence.supports_claim
            else "CONTRADICTS"
        )

        print(f"\n[{status}]")
        print(evidence.source_title)
        print(evidence.explanation)

    print("\nSOURCES:")

    for index, source in enumerate(
        citations,
        start=1
    ):

        print(
            f"{index}. {source['title']}"
        )

        print(
            f"   {source['url']}"
        )

    print("\n" + "=" * 60)


def main():

    print("=" * 60)
    print("              TRUTHLENS")
    print("       AI FACT VERIFICATION AGENT")
    print("=" * 60)

    agent = TruthLensAgent()
    verifier = Verifier(agent)

    while True:

        claim = input(
            "\nClaim > "
        ).strip()

        if claim.lower() == "exit":
            break

        if not claim:
            continue

        try:

            print("\nSearching and verifying...")

            data = verifier.verify_claim(claim)

            display_result(data)

        except Exception as error:

            print("\nSomething went wrong:")
            print(error)


if __name__ == "__main__":
    main()