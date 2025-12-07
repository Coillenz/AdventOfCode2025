package com.main.part2;

public class Dial {
    private static final int MAX_DIAL_VALUE = 100;

    private int currentPointer;

    public Dial(int currentPointer) {
        this.currentPointer = currentPointer;
    }
    
    /**
     * Turns the dial left
     * @param distance The distance to turn the dial
     * @return The amount of times the dial passed 0 (passed and hit)
     */
    public int turnLeft(int distance) {
        int oldPointer = this.currentPointer;
        int effectiveDistance = distance % MAX_DIAL_VALUE;
        this.currentPointer = (currentPointer - effectiveDistance + MAX_DIAL_VALUE) % MAX_DIAL_VALUE;

        // Check zero hit count for turning the dial left
        return this.checkZeroHitCountLeft(oldPointer, distance);
    }

    public int turnRight(int distance) {
        int oldPointer = this.currentPointer;
        int effectiveDistance = distance % MAX_DIAL_VALUE;
        this.currentPointer = (this.currentPointer + effectiveDistance) % MAX_DIAL_VALUE;

        // Check zero hit count for turning the dial left   
        return this.checkZeroHitCountRight(oldPointer, distance);
    }

    public boolean isAtPosZero() {
        return this.currentPointer == 0;
    }

    public int getCurrentPointer() {
        return currentPointer;
    }

    private int checkZeroHitCountLeft(int pointer, int distance) {
        return Math.floorDiv((pointer - 1), 100) - Math.floorDiv((pointer - distance - 1), MAX_DIAL_VALUE);
    }

    private int checkZeroHitCountRight(int pointer, int distance) {
        return Math.floorDiv(pointer + distance, MAX_DIAL_VALUE);
    }
}
