def destroy_walls(wall_health):
    for health_points in wall_health:
        if health_points <= 0:
            wall_health.remove(health_points)
    return wall_health
