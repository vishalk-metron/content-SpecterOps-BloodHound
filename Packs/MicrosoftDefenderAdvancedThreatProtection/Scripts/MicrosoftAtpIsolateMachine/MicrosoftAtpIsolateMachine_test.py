from pytest_mock import MockerFixture


def test_main(mocker: MockerFixture):
    """
    Given:
        Command args.
    When:
        Calling `main`.
    Assert:
        Ensure `execute_polling_command` is called once with the correct command name and args.
    """
    from MicrosoftAtpIsolateMachine import main

    args = {"machine_id": "machineA", "isolation_type": "Full"}
    mocker.patch("MicrosoftAtpIsolateMachine.demisto.args", return_value=args)
    mock_execute_polling_command = mocker.patch("MicrosoftAtpIsolateMachine.execute_polling_command", return_value=[])

    main()

    assert mock_execute_polling_command.call_count == 1
    assert mock_execute_polling_command.call_args[0] == ("microsoft-atp-isolate-machine", args)
