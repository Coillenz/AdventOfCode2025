package com.cobase.part2;

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
        this.currentPointer = Math.abs(currentPointer - (distance % MAX_DIAL_VALUE) + MAX_DIAL_VALUE) % MAX_DIAL_VALUE;
        
        // Check zero hit count for turning the dial left
        int zeroHitCount = this.checkZeroHitCount(oldPointer, distance);
        if (this.currentPointer == 0) {
            return zeroHitCount + 1;
        }

        return zeroHitCount;
    }

    public int turnRight(int distance) {
        int oldPointer = this.currentPointer;
        this.currentPointer = (this.currentPointer + (distance % MAX_DIAL_VALUE)) % MAX_DIAL_VALUE;

        // Check zero hit count for turning the dial left   
        int zeroHitCount = this.checkZeroHitCount(oldPointer, distance);
        if (this.currentPointer == 0) {
            return zeroHitCount + 1;
        }
        
        return zeroHitCount;
    }

    public boolean isAtPosZero() {
        return this.currentPointer == 0;
    }

    public int getCurrentPointer() {
        return currentPointer;
    }

    private int checkZeroHitCount(int pointer, int distance) {
        return Math.floorDiv(pointer + distance, MAX_DIAL_VALUE - 1);
    }
}
