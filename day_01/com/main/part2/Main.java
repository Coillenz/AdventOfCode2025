package com.main.part2;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.logging.FileHandler;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

public class Main {
    private static final String REAL_INPUT_PATH = "day_01/real-input.txt";

    private static final Logger logger = Logger.getLogger("Main");

    public static void main(String[] args) throws IOException {
        Path inputPath = Path.of(REAL_INPUT_PATH);
        String input = Files.readString(inputPath);
        Dial dial = new Dial(50);

        FileHandler handler = new FileHandler("day_01/output.txt", false);
        SimpleFormatter formatter = new SimpleFormatter();
        handler.setFormatter(formatter);
        logger.addHandler(handler);

        int password = 0;
        for (String line : input.lines().toList()) {
            int oldPointer = dial.getCurrentPointer();
            char direction = line.charAt(0);
            int distance = Integer.parseInt(line.substring(1));
            
            switch (direction) {
                case 'L':
                    password += dial.turnLeft(distance);
                    break;
                case 'R':
                    password += dial.turnRight(distance);
                    break;
                default:
                    throw new UnsupportedOperationException();
            }

            String debugMessage = String.format("%d -> move: %s%d pwd: %d -> %d%n", oldPointer, direction, distance, password,
                    dial.getCurrentPointer());

            logger.info(debugMessage);
        }

        String finalPassword = String.format("Password: %d", password);
        logger.info(finalPassword);
    }
}
