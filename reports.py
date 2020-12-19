import os


def exit_code(code: int) -> None:
    import sys
    sys.exit(code)


def prepare_report(reports_list: [str]) -> dict:
    response_dict = {}
    for report in reports_list:
        response_dict[report] = []
        try:
            with open('./pyscan/' + report) as f:
                lines = f.read().splitlines()
                for line in lines:
                    if not line.startswith('*'):
                        response_dict[report].append(line)
        except Exception as e:
            print('Exception caught ---->', e)
            exit_code(1)
    return response_dict


def main():
    reports_list = os.listdir('./pyscan/')
    print(prepare_report(reports_list))


if __name__ == '__main__':
    main()
